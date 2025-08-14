from pathlib import Path
import os

def build_prompt(context: str, question: str) -> str:
    # Charger un modèle de prompt si tu veux l'externaliser
    template_path = Path(__file__).parent / "rag_prompt.txt"
    if template_path.exists():
        template = template_path.read_text(encoding="utf-8")
        return template.format(context=context, question=question)

    # Sinon, prompt par défaut amélioré
    return f"""Tu es un assistant spécialisé en énergie (électricité, CO₂, bâtiments) avec accès à une base de connaissances spécifique sur le campus IIT Delhi.

IMPORTANT: Réponds UNIQUEMENT à partir du contexte fourni ci-dessous. Si l'information n'est pas dans le contexte, dis-le clairement.

INSTRUCTIONS:
1. Utilise EXCLUSIVEMENT les données du contexte fourni
2. Cite les variables exactes mentionnées (ex: "electricity kwh", "CO2 total", "temperature")
3. Donne les unités quand elles sont disponibles
4. Si tu trouves des informations sur la relation consommation-température, détaille-les
5. Si l'information n'est pas dans le contexte, dis "Cette information n'est pas disponible dans le contexte fourni"

Contexte:
{context}

Question: {question}

Réponse basée uniquement sur le contexte:"""
