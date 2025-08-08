# 🤖 InsightIQ

InsightIQ is a locally running, AI-powered internal knowledge assistant that lets you **ask natural language questions from your own PDF documents**. Powered by fast open-source LLMs via [Ollama](https://ollama.com), this tool is designed to break data silos and unlock insights instantly.

---

## 🚀 Features

- 📄 Upload PDFs directly through the UI
- 🧠 Text is chunked and embedded with `sentence-transformers`
- ⚡ Fast semantic search using FAISS vector store
- 🤖 Query answers using local LLMs (e.g., Mistral, TinyLlama, LLaMA3, Gemma)
- 💬 Clean Streamlit UI with chat history and timestamps
- 📥 All data stays on your machine

---

## 🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Ollama](https://ollama.com/) (for running local LLMs)

---

## 📦 Installation

1. **Clone the repo:**
```bash
git clone https://github.com/your-username/insightiq.git
cd insightiq
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Install and run Ollama:**  
[Download Ollama](https://ollama.com/download) and install a model, e.g.:
```bash
ollama run mistral
```

5. **Run the app:**
```bash
streamlit run app.py
```

---

## 📂 Folder Structure
```
├── app.py                  # Main Streamlit interface
├── chat_engine.py          # Handles QA interaction with models
├── embed_docs.py           # Document loader & splitter
├── vector_store.py         # Embeddings + FAISS indexing
├── sample_docs/            # Folder for user PDFs
├── faiss_index/            # Generated vector store
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📸 Demo

### App Screenshots

#### Landing Page
![Landing Page](Images/Landing_Page.png)
*The main dashboard of InsightIQ, showing the app title and a clean interface for document Q&A.*

#### File Upload
![File Upload](Images/File_Upload.png)
*Upload your PDF documents directly through the sidebar for instant knowledge ingestion.*

#### Model Types
![Model Types](Images/Model_Types.png)
*Select from available local LLMs (Mistral, TinyLlama, Llama3, Gemma) to power your Q&A.*

#### Thinking Spinner
![Thinking](Images/Thinking.png)
*A spinner animation appears while the app processes your question and generates an answer.*

#### Answer Display
![Answer](Images/Answer.png)
*Answers are displayed in a highlighted box, with chat history saved in the sidebar for reference.*

---

## 👨‍💻 Author
Built by [Aman Keskar](https://linkedin.com/in/aman-keskar) — Master's in Information Systems, Syracuse University.

---

## ⚖️ License
MIT License

---

## 🙌 Contribute / Feedback
PRs and feedback are welcome! Feel free to fork the repo or open issues for improvements.
