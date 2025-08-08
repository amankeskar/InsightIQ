# main.py

from loader import load_and_split_all_docs
from vector_store import create_faiss_index

# Load + split
chunks = load_and_split_all_docs("sample_docs")

# Create embeddings and store in FAISS
create_faiss_index(chunks)
