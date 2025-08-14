energy-assistant/
├── data/
│   ├── pdf/
│   │   └── rapport_energie.pdf
│   ├── csv/
│   │   └── mesures_energie.csv
│  
├── 
├── rag/
│   ├── ingest_csv.py
│   ├── ingest_pdf.py
│   └── faiss_index/
├── app/
│   ├── rag_prompt.txt
│   ├── app.py
│   ├── prompt_builder.py
│   └── mistral_client.py
├── requirements.txt
└── README.md

******************
UTILISATEUR → (Streamlit)
    |
    v
Question ------------------> [retrieval CSV avec FAISS]
    |                                 |
    v                                 v
  Contexte (chunks CSV)       Mistral fine-tuné (PDF)
    |                                 |
    └----------- PROMPT FINAL --------┘
                     |
                     v
               Réponse finale
*********************************************
# Assistant Énergétique

Prototype d’assistant IA basé sur :
- **Fine-tuning** de Mistral sur PDF (LoRA)
- **RAG** sur CSV (FAISS + Hugging Face embeddings)
- Interface **Streamlit** en mode Serverless

## Installation
```bash
pip install -r requirements.txt
python fine_tune/prepare_dataset.py
python fine_tune/train_lora.py
python rag/ingest_csv.py

streamlit run app/main.py
EMB_MODEL=sentence-transformers/all-MiniLM-L6-v2
FAISS_INDEX=rag/faiss_index/index_all.faiss
CHUNKS_PATH=rag/faiss_index/chunks_all.txt
META_PATH=rag/faiss_index/metadata_all.json
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=mistral
TOP_K=5
