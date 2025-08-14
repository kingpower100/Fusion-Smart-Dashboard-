import os
from pathlib import Path
import json
import faiss
import streamlit as st
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from prompt_builder import build_prompt
from mistral_client import query_mistral

# --------- Load config ---------
load_dotenv()

# Configuration avec valeurs par défaut
EMB_MODEL = os.getenv("EMB_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
INDEX_PATH = Path(os.getenv("FAISS_INDEX", "rag/faiss_index/index_all.faiss"))
CHUNKS_PATH = Path(os.getenv("CHUNKS_PATH", "rag/faiss_index/chunks_all.txt"))
META_PATH = Path(os.getenv("META_PATH", "rag/faiss_index/metadata_all.json"))
TOP_K = int(os.getenv("TOP_K", 15))

# Index PDF dédiés
PDF_INDEX_PATH = Path(os.getenv("FAISS_INDEX_PDF", "rag/faiss_index/index_pdf.faiss"))
PDF_CHUNKS_PATH = Path(os.getenv("FAISS_INDEX_PDF_PATH", "rag/faiss_index/chunks_pdf.txt"))

# --------- Load FAISS & data ---------
@st.cache_resource(ttl=3600)  # Cache for 1 hour
def load_index_and_data():
    try:
        with st.spinner("🔄 Chargement des index FAISS..."):
            index = faiss.read_index(str(INDEX_PATH))
            chunks = CHUNKS_PATH.read_text(encoding="utf-8").splitlines()
            metadata = json.loads(META_PATH.read_text(encoding="utf-8"))
            
        with st.spinner("🔄 Chargement du modèle d'embedding..."):
            embedder = SentenceTransformer(EMB_MODEL)
            
        st.success("✅ Index et modèle chargés avec succès!")
        return index, chunks, metadata, embedder
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement: {str(e)}")
        st.stop()

@st.cache_resource(ttl=3600)  # Cache for 1 hour
def load_pdf_index_and_chunks():
    try:
        with st.spinner("🔄 Chargement des index PDF..."):
            index_pdf = faiss.read_index(str(PDF_INDEX_PATH))
            chunks_pdf = PDF_CHUNKS_PATH.read_text(encoding="utf-8").splitlines()
        return index_pdf, chunks_pdf
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement PDF: {str(e)}")
        st.stop()

# Cache global pour éviter les rechargements
if 'models_loaded' not in st.session_state:
    st.session_state.models_loaded = False
    st.session_state.index = None
    st.session_state.chunks = None
    st.session_state.metadata = None
    st.session_state.embedder = None
    st.session_state.index_pdf = None
    st.session_state.chunks_pdf = None

# --------- Search function ---------
def search_chunks(query: str, embedder, index, chunks, metadata, k: int = TOP_K):
    q_emb = embedder.encode([query], convert_to_numpy=True).astype("float32")
    D, I = index.search(q_emb, k)
    results = []
    for dist, idx in zip(D[0], I[0]):
        if idx == -1:
            continue
        results.append({
            "text": chunks[idx],
            "metadata": metadata[idx],
            "distance": float(dist)
        })
    # Fallback: élargir la recherche si vide
    if not results and k < 15:
        return search_chunks(query, embedder, index, chunks, metadata, k=15)
    return results

def search_chunks_pdf(query: str, embedder, index_pdf, chunks_pdf, k: int = min(TOP_K, 8)):
    # 1. Multi-query: générer des variantes de la requête
    query_variants = generate_query_variants(query)
    
    # 2. Recherche vectorielle pour chaque variante
    all_results = []
    for variant in query_variants:
        q_emb = embedder.encode([variant], convert_to_numpy=True).astype("float32")
        D, I = index_pdf.search(q_emb, k)
        for dist, idx in zip(D[0], I[0]):
            if idx == -1:
                continue
            all_results.append({
                "text": chunks_pdf[idx],
                "metadata": {"source": "pdf", "row": int(idx), "variant": variant},
                "distance": float(dist)
            })
    
    # 3. Recherche par mots-clés ciblée (priorité maximale)
    priority_keywords = [
        "consommation électrique vs température", "consommation vs température",
        "température extérieure", "température ext", "température extérieure",
        "zone de confort thermique", "confort thermique",
        "chauffage", "refroidissement", "climatisation"
    ]
    
    keyword_results = []
    for i, chunk in enumerate(chunks_pdf):
        chunk_lower = chunk.lower()
        # Vérifier les mots-clés prioritaires exacts
        for keyword in priority_keywords:
            if keyword.lower() in chunk_lower:
                keyword_results.append({
                    "text": chunk,
                    "metadata": {"source": "pdf", "row": i, "method": "exact_keyword", "keyword": keyword},
                    "distance": 0.0  # Priorité maximale
                })
                break
    
    # 4. Recherche par mots-clés secondaires
    secondary_keywords = ["température", "temperature", "consommation", "kwh", "campus", "iit"]
    for i, chunk in enumerate(chunks_pdf):
        chunk_lower = chunk.lower()
        if any(keyword in chunk_lower for keyword in secondary_keywords):
            # Vérifier qu'on n'a pas déjà ce chunk
            if not any(r["text"] == chunk for r in keyword_results):
                keyword_results.append({
                    "text": chunk,
                    "metadata": {"source": "pdf", "row": i, "method": "secondary_keyword"},
                    "distance": 0.1
                })
    
    # 5. Fusion et déduplication
    final_results = keyword_results + all_results
    
    # Supprimer les doublons en gardant la priorité
    seen_texts = set()
    unique_results = []
    for r in final_results:
        if r["text"] not in seen_texts:
            unique_results.append(r)
            seen_texts.add(r["text"])
        if len(unique_results) >= k + 15:  # Marge plus importante
            break
    
    return unique_results

def generate_query_variants(query: str):
    """Génère des variantes de la requête pour améliorer la recherche"""
    variants = [query]
    
    # Variantes avec synonymes
    if "consommation" in query.lower():
        variants.append(query.replace("consommation", "consommation électrique"))
        variants.append(query.replace("consommation", "kwh"))
    
    if "température" in query.lower():
        variants.append(query.replace("température", "température extérieure"))
        variants.append(query.replace("température", "climat"))
    
    if "campus" in query.lower():
        variants.append(query.replace("campus", "IIT Delhi"))
        variants.append(query.replace("campus", "bâtiments"))
    
    # Variante en anglais si pertinent
    if any(word in query.lower() for word in ["consommation", "température", "campus"]):
        english_variant = query.replace("consommation", "consumption").replace("température", "temperature").replace("campus", "campus")
        variants.append(english_variant)
    
    return list(set(variants))  # Supprimer les doublons

# --------- RAG function ---------
def rag_answer(question: str, embedder, index, chunks, metadata, index_pdf, chunks_pdf):
    # Recherche silencieuse dans l'index principal et PDF
    results_all = search_chunks(question, embedder, index, chunks, metadata)
    results_pdf = search_chunks_pdf(question, embedder, index_pdf, chunks_pdf)
    
    # Fusionner en priorisant le PDF
    merged = []
    seen_texts = set()
    
    # Ajouter d'abord les résultats PDF
    for r in results_pdf:
        if r["text"] not in seen_texts:
            merged.append(r)
            seen_texts.add(r["text"])
    
    # Ajouter ensuite les résultats de l'index principal
    for r in results_all:
        if r["text"] not in seen_texts:
            merged.append(r)
            seen_texts.add(r["text"])
        if len(merged) >= 12:  # Limiter le contexte
            break
    
    # Construire le contexte
    context = "\n\n".join([r["text"] for r in merged])
    
    # Créer le prompt avec le contexte
    prompt = build_prompt(context, question)
    
    # Générer la réponse
    answer = query_mistral(prompt)
    return answer, merged

# --------- General chat function ---------
def general_chat(message: str):
    prompt = f"""Tu es un assistant IA utile et amical. Réponds de manière naturelle et conversationnelle à l'utilisateur.

Message de l'utilisateur: {message}

Réponse:"""
    return query_mistral(prompt)

# --------- Smart response function ---------
def smart_response(message: str, embedder, index, chunks, metadata, index_pdf, chunks_pdf):
    # Mots-clés liés à l'énergie pour déclencher le RAG (avec variantes sans accents + campus/IIT)
    energy_keywords = [
        'énergie', 'energie', 'électricité', 'electricite', 'électrique', 'electrique',
        'consommation', 'kwh', 'kw', 'watts', 'watt', 'co2', 'carbone', 'émissions', 'emissions',
        'gaz à effet de serre', 'gaz a effet de serre', 'climat', 'thermique', 'chauffage',
        'refroidissement', 'ventilation', 'hvac', 'climatisation',
        'efficacité énergétique', 'efficacite energetique', 'audit énergétique', 'audit energetique',
        'performance énergétique', 'performance energetique', 'bâtiment', 'batiment', 'bâtiments', 'batiments',
        'campus', 'iit', 'temperature', 'température', 'meteo', 'météo'
    ]
    
    message_lower = message.lower()
    
    # Vérifier si le message contient des mots-clés liés à l'énergie
    if any(keyword in message_lower for keyword in energy_keywords):
        # Utiliser le RAG pour les questions liées à l'énergie
        return rag_answer(message, embedder, index, chunks, metadata, index_pdf, chunks_pdf)
    else:
        # Réponse générale pour les autres messages
        answer = general_chat(message)
        return answer, None

# --------- Main function ---------
def run_energy_assistant():
    """Main function to run the energy assistant - can be imported and called from other apps"""
    
    # Load FAISS & data with global caching
    if not st.session_state.models_loaded:
        try:
            with st.spinner("🔄 Chargement initial des modèles (cela ne se fera qu'une fois par session)..."):
                st.session_state.index, st.session_state.chunks, st.session_state.metadata, st.session_state.embedder = load_index_and_data()
                st.session_state.index_pdf, st.session_state.chunks_pdf = load_pdf_index_and_chunks()
                st.session_state.models_loaded = True
                st.success("✅ Modèles chargés et mis en cache!")
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement des index: {str(e)}")
            return
    else:
        # Use cached models
        index, chunks, metadata, embedder = st.session_state.index, st.session_state.chunks, st.session_state.metadata, st.session_state.embedder
        index_pdf, chunks_pdf = st.session_state.index_pdf, st.session_state.chunks_pdf
        
        # Vérification silencieuse des index
        if index.ntotal == 0:
            st.error("❌ Index principal vide - problème de chargement")
        if index_pdf.ntotal == 0:
            st.error("❌ Index PDF vide - problème de chargement")
        if len(chunks_pdf) == 0:
            st.error("❌ Chunks PDF vides - problème de chargement")

    # --------- Streamlit UI ---------
    st.title("🤖 Assistant IA - Général + Spécialisé Énergie")
    st.markdown("Chattez librement avec l'assistant. Il répondra de manière générale et utilisera sa base de connaissances spécialisée pour les questions sur l'énergie.")

    # Initialiser l'historique des conversations
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afficher l'historique des conversations
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Interface de saisie
    if prompt := st.chat_input("Écrivez votre message..."):
        # Ajouter le message utilisateur
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Générer la réponse intelligente
        with st.chat_message("assistant"):
            with st.spinner("🤔 Réflexion en cours..."):
                answer, sources = smart_response(prompt, embedder, index, chunks, metadata, index_pdf, chunks_pdf)
            
            # Afficher la réponse uniquement
            st.markdown(answer)
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({"role": "assistant", "content": answer})

# --------- Main execution (only when run directly) ---------
if __name__ == "__main__":
    st.set_page_config(page_title="Assistant IA", page_icon="🤖", layout="wide")
    run_energy_assistant()

  