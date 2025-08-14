"""
Script de préchargement des modèles pour améliorer les performances
"""
import os
import sys
import time
import faiss
from sentence_transformers import SentenceTransformer

def preload_models():
    """Précharge les modèles et les met en cache"""
    print("🚀 Préchargement des modèles pour améliorer les performances...")
    
    # Ajouter le chemin vers energy-assistant
    current_dir = os.path.dirname(__file__)
    energy_assistant_path = os.path.abspath(os.path.join(current_dir, "..", "..", "energy-assistant"))
    
    if energy_assistant_path not in sys.path:
        sys.path.insert(0, energy_assistant_path)
    
    # Chemins des fichiers
    index_path = os.path.join(energy_assistant_path, "rag", "faiss_index", "index_all.faiss")
    chunks_path = os.path.join(energy_assistant_path, "rag", "faiss_index", "chunks_all.txt")
    metadata_path = os.path.join(energy_assistant_path, "rag", "faiss_index", "metadata_all.json")
    
    pdf_index_path = os.path.join(energy_assistant_path, "rag", "faiss_index", "index_pdf.faiss")
    pdf_chunks_path = os.path.join(energy_assistant_path, "rag", "faiss_index", "chunks_pdf.txt")
    
    try:
        print("📚 Chargement de l'index principal...")
        start_time = time.time()
        index = faiss.read_index(index_path)
        print(f"✅ Index principal chargé en {time.time() - start_time:.2f}s")
        
        print("📖 Chargement des chunks...")
        start_time = time.time()
        with open(chunks_path, 'r', encoding='utf-8') as f:
            chunks = f.read().splitlines()
        print(f"✅ Chunks chargés en {time.time() - start_time:.2f}s")
        
        print("📋 Chargement des métadonnées...")
        start_time = time.time()
        import json
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        print(f"✅ Métadonnées chargées en {time.time() - start_time:.2f}s")
        
        print("🤖 Chargement du modèle d'embedding...")
        start_time = time.time()
        embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print(f"✅ Modèle d'embedding chargé en {time.time() - start_time:.2f}s")
        
        print("📄 Chargement de l'index PDF...")
        start_time = time.time()
        index_pdf = faiss.read_index(pdf_index_path)
        print(f"✅ Index PDF chargé en {time.time() - start_time:.2f}s")
        
        print("📝 Chargement des chunks PDF...")
        start_time = time.time()
        with open(pdf_chunks_path, 'r', encoding='utf-8') as f:
            chunks_pdf = f.read().splitlines()
        print(f"✅ Chunks PDF chargés en {time.time() - start_time:.2f}s")
        
        print("\n🎯 Tous les modèles sont préchargés et prêts!")
        print("💡 Les prochaines exécutions seront beaucoup plus rapides!")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors du préchargement: {str(e)}")
        return False

if __name__ == "__main__":
    preload_models()
