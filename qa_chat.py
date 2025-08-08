import subprocess
import os
import requests
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def ensure_model_available(model_name):
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, shell=True)
        if model_name.lower() not in result.stdout.lower():
            print(f"\n📥 Model '{model_name}' not found. Pulling it now...")
            pull = subprocess.run(["ollama", "pull", model_name], shell=True)
            if pull.returncode != 0:
                print("❌ Failed to pull the model from Ollama. Please check the model name.")
                return False
        else:
            print(f"✅ Model '{model_name}' is already available.")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def ask_question_with_model(user_question, model_name):
    # Ensure model is pulled
    if not ensure_model_available(model_name):
        return "❌ Model not ready."

    # Load vector DB
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

    # Retrieve top chunks
    docs = vectorstore.similarity_search(user_question, k=3)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""Use the following context to answer the question:\n\n{context}\n\nQuestion: {user_question}\nAnswer:"""

    # Send request to Ollama directly
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model_name, "prompt": prompt, "stream": False}
        )

        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        elif response.status_code == 403:
            return "🚫 Access denied (403). Make sure Ollama is running and accessible."
        else:
            return f"❌ Error {response.status_code}: {response.text}"

    except requests.exceptions.ConnectionError:
        return "❌ Could not connect to Ollama at http://localhost:11434. Is it running?"

