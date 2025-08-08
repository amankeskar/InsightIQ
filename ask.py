from qa_chat import ask_question_with_model

# Prompt for model selection at the beginning
print("🤖 Available models: mistral, tinyllama, llama3, gemma:2b, etc.")
selected_model = input("📌 Enter the model name you want to use: ").strip()

while True:
    query = input("\n❓ Ask a question (or type 'exit'): ")
    if query.lower() in ['exit', 'quit']:
        break
    print(ask_question_with_model(query, selected_model))
