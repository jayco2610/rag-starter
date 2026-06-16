# RAG Starter — AI assistant that answers only from your documents

A RAG (Retrieval-Augmented Generation) assistant in Python.
Give it any text document → ask questions → get answers based only on that document. No guessing, no made-up facts.

**Live demo (real company, real data):** [МИА.РФ dental clinic assistant](https://huggingface.co/spaces/rag-jasur/mia-clinic-assistant) — answers patient questions about pricing, services, and hours, available 24/7.

---

## What it does

```
You: "Сколько стоит имплант под ключ?"
AI:  "От 45 000 рублей." ← taken directly from the clinic's own document
```

If the question is outside the document, it doesn't hallucinate — it points the user to the clinic's site or contact info instead.

---

## Two versions in this repo

**1. Local version (`app_local.py`)** — fully offline, no API keys, no cloud. Runs on Ollama with `llama3.1:8b` on your own machine. Good for development and privacy-sensitive use cases.

**2. Production version (`hf_space/`)** — what's actually deployed and live. Uses Groq's free API (`llama-3.1-8b-instant`) for speed, a Gradio chat interface, and runs 24/7 on Hugging Face Spaces — no server, no local machine required.

---

## Tech stack

- **Python 3.x**
- **Ollama** + **llama3.1:8b** — local model for offline dev
- **Groq API** — fast, free cloud inference for the live deploy
- **Gradio** — browser chat interface
- **Hugging Face Spaces** — free 24/7 hosting

---

## Run the local version

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

**4. Run**

```bash
python3 app_local.py
```

Type any question about the document. Type `выход` or `exit` to quit.

---

## Use cases

- Customer support bot for a clinic, shop, or service
- Internal knowledge base assistant
- FAQ automation from any text file

---

## Why this exists

Built as a working portfolio piece — a real example of grounded, no-hallucination AI for a real business (a dental clinic chain), not a toy demo. Used as a reference case for AI consulting work.

---

Built by [Jasur Akhmadaliev](https://jasur-portfolio-pied.vercel.app) — PM building AI tools in public.
