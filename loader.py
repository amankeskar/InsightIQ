# loader.py

import os
import fitz  # This comes from PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split large text into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return splitter.split_text(text)

def load_and_split_all_docs(folder_path: str) -> List[str]:
    """Load and split all files in the sample_docs folder."""
    all_chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf") or filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(f"Loading {file_path}...")
            if filename.endswith(".pdf"):
                raw_text = load_pdf(file_path)
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    raw_text = f.read()
            chunks = split_text(raw_text)
            all_chunks.extend(chunks)
    return all_chunks
