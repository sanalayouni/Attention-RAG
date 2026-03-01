# 🤖 Attention-RAG

> A local Retrieval-Augmented Generation (RAG) chatbot that answers questions about the **"Attention Is All You Need"** paper — powered by HuggingFace embeddings and LLaMA 3 via Ollama. No cloud APIs. No API keys. Just local inference.

---

## 📌 Overview

This project is a hands-on RAG pipeline built for learning purposes. Ask natural language questions about the original 2017 Transformer paper, and the chatbot will retrieve the most relevant context and generate accurate, grounded answers — all running locally on your machine.

**Paper:** *Attention Is All You Need* — Vaswani et al., 2017

---

## 🧠 Architecture

The pipeline follows a classic RAG pattern:

```
PDF Document
    ↓
Chunk Splitting
    ↓
HuggingFace Embeddings
    ↓
ChromaDB Vector Store
    ↓
Semantic Retrieval (on query)
    ↓
LLaMA 3 (via Ollama) → Answer
```

1. **Load** the PDF document
2. **Split** it into overlapping text chunks
3. **Embed** chunks using a HuggingFace sentence transformer
4. **Store** embeddings in ChromaDB
5. **Retrieve** the top-k relevant chunks for each user query
6. **Generate** an answer using LLaMA 3 running locally via Ollama

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Embeddings | HuggingFace Sentence Transformers |
| LLM | LLaMA 3 (via Ollama) |
| Vector Store | ChromaDB |
| PDF Parsing | LangChain / PyMuPDF |

---

## 🔐 Why Local LLM?

Running the model locally with Ollama means:

- ✅ No external API calls
- ✅ No API key required
- ✅ Full control over inference
- ✅ Better data privacy
- ✅ Great for learning LLM internals

---

## 📂 Project Structure

```
Attention-RAG/
│
├── chatbot.py               # Main chatbot entry point
├── data/
│   └── attention_is_all_you_need.pdf
├── vector_store/            # Persisted ChromaDB embeddings
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/sanalayouni/Attention-RAG.git
cd Attention-RAG
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Download Ollama from [https://ollama.com](https://ollama.com), then pull the LLaMA 3 model:

```bash
ollama pull llama3
```

Make sure Ollama is running in the background before launching the chatbot.

### 5. Run the chatbot

```bash
python chatbot.py
```

---

## 💬 Example Queries

```
What is the main idea behind self-attention?
Why are positional encodings necessary in the Transformer?
How does multi-head attention work?
What are the encoder and decoder components of the Transformer?
```

---

## 🎯 Features

- 📄 Document-grounded question answering
- 🦙 Fully local LLM inference (LLaMA 3 via Ollama)
- 🔍 Semantic search with vector embeddings
- 🗄️ Persistent vector store with ChromaDB
- 🔒 No cloud API usage

---

## 📚 What I Learned

Building this project deepened my understanding of:

- RAG pipeline design and implementation
- Embeddings and vector similarity search
- The Transformer architecture (from the source!)
- Running LLMs locally with Ollama
- Building AI systems without relying on cloud APIs

---

## 🔮 Roadmap

- [ ] Support for multiple documents
- [ ] Conversational memory across turns
- [ ] Streamlit web interface
- [ ] Docker containerization
- [ ] Evaluation metrics (faithfulness, relevance)

---

## 👩‍💻 Author

**Sana Layouni** — Software Engineering Student

[![GitHub](https://img.shields.io/badge/GitHub-sanalayouni-181717?logo=github)](https://github.com/sanalayouni)
