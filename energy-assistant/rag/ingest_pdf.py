# rag/ingest_pdf.py
import os
from pathlib import Path
import numpy as np
import pandas as pd  # only for convenient text batching, no CSV reading here
import faiss
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

# ------------ Config ------------
BASE_DIR   = Path(__file__).resolve().parent.parent
PDF_PATH   = BASE_DIR / "data" / "pdf" / "rapport_energie.pdf"
INDEX_DIR  = BASE_DIR / "rag" / "faiss_index"
MODEL_EMB  = "sentence-transformers/all-MiniLM-L6-v2"

# batching to avoid VRAM/RAM spikes
ENCODE_BATCHSIZE = 128   # lower if you hit CUDA OOM: 128 -> 64 -> 32
CHUNK_SIZE_CHARS = 800   # split long text into ~800-char chunks
DEVICE = "cuda"          # "cuda" for your GTX 1650; fallback to "cpu" if needed

# output filenames (do NOT overwrite CSV index)
INDEX_OUT  = INDEX_DIR / "index_pdf.faiss"
CHUNKS_OUT = INDEX_DIR / "chunks_pdf.txt"

# ------------ Prep ------------
os.makedirs(INDEX_DIR, exist_ok=True)

# Try to use GPU, fall back cleanly
try:
    import torch
    if not torch.cuda.is_available():
        DEVICE = "cpu"
except Exception:
    DEVICE = "cpu"

model = SentenceTransformer(MODEL_EMB, device=DEVICE)
dim = model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dim)

# ------------ Read & extract PDF text ------------
if not PDF_PATH.exists():
    raise FileNotFoundError(f"PDF not found: {PDF_PATH}")

reader = PdfReader(str(PDF_PATH))
pages = reader.pages  # <-- iterate over pages

# Extract text page by page, ignoring Nones
page_texts = []
for i, page in enumerate(pages):
    try:
        t = page.extract_text()
        if t:
            page_texts.append(t)
    except Exception as e:
        print(f"⚠️ Could not extract page {i}: {e}")

full_text = "\n".join(page_texts).strip()
if not full_text:
    raise ValueError("No extractable text found in the PDF. "
                     "If the PDF is scanned, use OCR first (e.g., OCRmyPDF/Tesseract).")

# ------------ Chunking ------------
# Simple fixed-size chunking; you can replace with sentence-based splitter later.
chunks = [full_text[i:i+CHUNK_SIZE_CHARS] for i in range(0, len(full_text), CHUNK_SIZE_CHARS)]

# ------------ Batched encode + build index ------------
# Start fresh chunks file
open(CHUNKS_OUT, "w", encoding="utf-8").close()

total = 0
for start in range(0, len(chunks), ENCODE_BATCHSIZE):
    batch = chunks[start:start+ENCODE_BATCHSIZE]

    # encode -> float32 for FAISS
    emb = model.encode(
        batch,
        batch_size=min(ENCODE_BATCHSIZE, len(batch)),
        convert_to_numpy=True,
        show_progress_bar=False,
        normalize_embeddings=False,   # keep L2 semantics
    ).astype(np.float32)

    index.add(emb)

    # append corresponding text lines
    with open(CHUNKS_OUT, "a", encoding="utf-8") as f:
        for line in batch:
            f.write(line.replace("\r", " ") + "\n")

    total += len(batch)
    print(f"✅ Encoded {total}/{len(chunks)} chunks (device={DEVICE})")

# ------------ Save index ------------
faiss.write_index(index, str(INDEX_OUT))
print(f"🎯 PDF index created: {INDEX_OUT.name} with {total} chunks")
print(f"🧾 Chunks saved to: {CHUNKS_OUT.name}")
