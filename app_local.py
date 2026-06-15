from langchain_ollama import OllamaLLM

MODEL = "llama3.1:8b"
DOC_PATH = "sample_doc.txt"

def load_document(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def ask(question: str, document: str) -> str:
    llm = OllamaLLM(model=MODEL)
    prompt = f"""Ты помощник клиники. Отвечай только на основе документа ниже.
Если ответа нет в документе — скажи об этом честно.

Документ:
{document}

Вопрос: {question}
Ответ:"""
    return llm.invoke(prompt)

def main():
    print(f"Загружаю документ: {DOC_PATH}")
    document = load_document(DOC_PATH)
    print("Готово. Задавай вопросы (введи 'выход' чтобы завершить)\n")

    while True:
        question = input("Вопрос: ").strip()
        if question.lower() in ("выход", "exit", "quit"):
            break
        if not question:
            continue
        print("\nОтвечаю...")
        answer = ask(question, document)
        print(f"\nОтвет: {answer}\n")

if __name__ == "__main__":
    main()
