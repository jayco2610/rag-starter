import gradio as gr
from langchain_ollama import OllamaLLM

MODEL = "llama3.1:8b"
DOC_PATH = "mia_clinic.txt"

with open(DOC_PATH, "r", encoding="utf-8") as f:
    DOCUMENT = f.read()

llm = OllamaLLM(model=MODEL)

def answer(question, history):
    if not question.strip():
        return ""
    prompt = f"""Ты вежливый помощник стоматологической клиники МИА.РФ.
Отвечай только на основе документа ниже. Будь конкретным — называй цены и условия.
Если ответа нет в документе — скажи об этом честно и предложи зайти на сайт miaclinic.ru.

Документ:
{DOCUMENT}

Вопрос пациента: {question}
Ответ помощника:"""
    return llm.invoke(prompt)

demo = gr.ChatInterface(
    fn=answer,
    title="МИА.РФ — AI-помощник клиники",
    description="Задайте вопрос о ценах, услугах и условиях лечения",
    examples=[
        "Сколько стоит имплант под ключ?",
        "Есть ли рассрочка?",
        "Какие гарантии на импланты?",
        "Сколько стоит лечение кариеса?",
        "Вы работаете в выходные?",
    ],
)

if __name__ == "__main__":
    demo.launch(inbrowser=True)
