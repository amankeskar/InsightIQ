import streamlit as st
from datetime import datetime
import os
from qa_chat import ask_question_with_model
from loader import load_and_split_all_docs
from vector_store import create_faiss_index

# --- App Config ---
st.set_page_config(
    page_title="📄 InsightIQ",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Custom Toast Notification Function ---
def show_custom_toast(message, color="#4BB543"):
    """Display a custom toast in the bottom-left corner that disappears after 4 seconds."""
    st.markdown(f"""
        <div style='position: fixed;
                    bottom: 20px;
                    left: 20px;
                    background-color: {color};
                    color: white;
                    padding: 12px 18px;
                    border-radius: 8px;
                    font-weight: 500;
                    z-index: 9999;
                    animation: fadeOut 4s forwards;'>
            {message}
        </div>
        <style>
        @keyframes fadeOut {{
            0% {{ opacity: 1; }}
            75% {{ opacity: 1; }}
            100% {{ opacity: 0; display: none; }}
        }}
        </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Chat History & Upload ---
with st.sidebar:
    st.title("🕘 Chat History")

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []  # list of dicts: {"time": str, "question": str}

    for entry in reversed(st.session_state.chat_log):
        st.markdown(f"- **{entry['time']}**\n  _{entry['question']}_")

    st.markdown("---")
    st.subheader("📄 Upload a PDF")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_file:
        file_path = os.path.join("sample_docs", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        show_custom_toast(f"'{uploaded_file.name}' uploaded successfully!")

        with st.spinner("🔄 Reprocessing documents..."):
            chunks = load_and_split_all_docs("sample_docs")
            create_faiss_index(chunks)
        show_custom_toast("✅ Knowledge base updated!")

# --- Main Interface ---
st.markdown("<h1 style='text-align: center;'>🤖 InsightIQ</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px;'>Ask questions from your own documents using local AI models.</p>", unsafe_allow_html=True)

model = st.selectbox(
    "🎛️ Choose a model",
    ["Mistral", "TinyLlama", "Llama3", "Gemma:2B"],
    index=0,
    help="These models run locally with Ollama."
)


# --- Streamlit input and button for Q&A ---
question = st.text_input("❓ Ask a question")

if st.button("🚀 Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("🤔 Thinking..."):
            answer = ask_question_with_model(question, model)
        st.markdown("---")
        st.markdown("### 💬 Answer")
        st.success(answer)
        current_time = datetime.now().strftime("%I:%M %p")
        st.session_state.chat_log.append({"time": current_time, "question": question})
