import faiss
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
INDEX_DIR = BASE_DIR / "faiss_index"

# Paths for CSV
FAISS_CSV_PATH   = INDEX_DIR / "index.faiss"
CHUNKS_CSV_PATH  = INDEX_DIR / "chunks.txt"

# Paths for PDF
FAISS_PDF_PATH   = INDEX_DIR / "index_pdf.faiss"
CHUNKS_PDF_PATH  = INDEX_DIR / "chunks_pdf.txt"

# Output merged
FAISS_ALL_PATH   = INDEX_DIR / "index_all.faiss"
CHUNKS_ALL_PATH  = INDEX_DIR / "chunks_all.txt"
META_ALL_PATH    = INDEX_DIR / "metadata_all.json"

# --- Load indexes ---
index_csv = faiss.read_index(str(FAISS_CSV_PATH))
index_pdf = faiss.read_index(str(FAISS_PDF_PATH))

# --- Load chunks ---
chunks_csv = Path(CHUNKS_CSV_PATH).read_text(encoding="utf-8").splitlines()
chunks_pdf = Path(CHUNKS_PDF_PATH).read_text(encoding="utf-8").splitlines()

# --- Create merged index ---
dim = index_csv.d
index_all = faiss.IndexFlatL2(dim)
index_all.add(index_csv.reconstruct_n(0, index_csv.ntotal))
index_all.add(index_pdf.reconstruct_n(0, index_pdf.ntotal))

# --- Create merged chunks ---
chunks_all = chunks_csv + chunks_pdf
Path(CHUNKS_ALL_PATH).write_text("\n".join(chunks_all), encoding="utf-8")

# --- Create metadata mapping ---
metadata = (
    [{"source": "csv", "row": i} for i in range(len(chunks_csv))] +
    [{"source": "pdf", "row": i} for i in range(len(chunks_pdf))]
)
Path(META_ALL_PATH).write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")

# --- Save merged index ---
faiss.write_index(index_all, str(FAISS_ALL_PATH))

print(f"✅ Merged index created with {len(chunks_all)} chunks")
print(f"   Saved to {FAISS_ALL_PATH.name}, {CHUNKS_ALL_PATH.name}, and {META_ALL_PATH.name}")
