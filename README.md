# RAG Starter — Local AI that reads your documents

A minimal RAG (Retrieval-Augmented Generation) script in Python.  
Give it any text document → ask questions → get answers based only on that document.

No cloud. No API keys. Runs fully offline on your Mac.

---

## What it does

```
You: "How much does an implant cost?"
AI:  "From 45,000 rubles." ← taken directly from the document
```

The model does not guess or hallucinate. It reads only what you give it.

---

## Tech stack

- **Python 3.x**
- **Ollama** — runs AI models locally
- **llama3.1:8b** — the model (4.9 GB, downloaded once)
- **langchain-ollama** — Python wrapper

---

## Setup

**1. Install Ollama**

Download from [ollama.com](https://ollama.com/download) and install.

**2. Pull the model**

```bash
ollama pull llama3.1:8b
```

**3. Clone and install dependencies**

```bash
git clone https://github.com/jayco2610/rag-starter.git
cd rag-starter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Run

```bash
source venv/bin/activate
python3 app_local.py
```

Then type any question about the document. Type `выход` or `exit` to quit.

---

## Use cases

- Customer support bot for a clinic, shop, or service
- Internal knowledge base assistant
- FAQ automation from any text file

---

## What's next

- [ ] Web interface (Gradio or Streamlit)
- [ ] Support for PDF documents
- [ ] Gemini API version (when available in region)

---

Built by [Jasur Akhmadaliev](https://jasur-portfolio-pied.vercel.app) — PM building AI tools in public.
