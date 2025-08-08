# vector_store.py (Free version using SentenceTransformers)

from sentence_transformers import SentenceTransformer
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_faiss_index(chunks):
    """Use FREE SentenceTransformers to create FAISS vector index."""
    print("🔄 Generating FREE embeddings and storing in FAISS...")

    # Wrap each chunk as a LangChain Document
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Load a free model from HuggingFace
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # Create the FAISS index
    faiss_db = FAISS.from_documents(docs, embedding)

    # Save the index to disk
    faiss_db.save_local("faiss_index")

    print("✅ Free embeddings stored successfully in 'faiss_index/'")
