import os
from pathlib import Path
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# ---------- Config ----------
BASE_DIR   = Path(__file__).resolve().parent.parent
CSV_PATH   = BASE_DIR / "data" / "csv" / "mesures_energie.csv"
INDEX_DIR  = BASE_DIR / "rag" / "faiss_index"
MODEL_EMB  = "sentence-transformers/all-MiniLM-L6-v2"

# Tune these two for low-power machines:
PANDAS_CHUNKSIZE = 500      # rows read from CSV at a time
ENCODE_BATCHSIZE = 64       # rows encoded by the model at a time
DEVICE = "cpu"              # "cpu" is safest; set to "cuda" if you have GPU

# ---------- Prep ----------
os.makedirs(INDEX_DIR, exist_ok=True)
model = SentenceTransformer(MODEL_EMB, device=DEVICE)
dim = model.get_sentence_embedding_dimension()
index = faiss.IndexFlatL2(dim)

chunks_txt_path = INDEX_DIR / "chunks.txt"
# Start a fresh chunks.txt
with open(chunks_txt_path, "w", encoding="utf-8") as _f:
    pass

total_rows = 0
part = 0

# ---------- Stream read + batched encode ----------
for df_part in pd.read_csv(CSV_PATH, chunksize=PANDAS_CHUNKSIZE):
    part += 1
    # Turn each row into a single string: "col1 | col2 | ... "
    rows_text = df_part.astype(str).agg(" | ".join, axis=1).tolist()

    # Encode in small batches to limit memory
    # (convert_to_numpy=True gives float32; show_progress_bar=False keeps it quiet)
    embeddings = model.encode(
        rows_text,
        batch_size=ENCODE_BATCHSIZE,
        convert_to_numpy=True,
        show_progress_bar=False,
        normalize_embeddings=False,   # keep L2 distance consistent
    ).astype(np.float32)

    # Add to FAISS index
    index.add(embeddings)

    # Append the corresponding text rows to chunks.txt
    with open(chunks_txt_path, "a", encoding="utf-8") as f:
        for line in rows_text:
            f.write(line + "\n")

    total_rows += len(rows_text)
    print(f"✅ Processed chunk {part}: +{len(rows_text)} rows (total={total_rows})")

# ---------- Save index ----------
faiss.write_index(index, str(INDEX_DIR / "index.faiss"))
print(f"🎯 Index CSV créé: {total_rows} lignes encodées en batches "
      f"(chunksize={PANDAS_CHUNKSIZE}, batch_size={ENCODE_BATCHSIZE})")
