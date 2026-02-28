# Attention-RAG
A local Retrieval-Augmented Generation (RAG) chatbot built with Hugging Face embeddings and LLaMA 3 via Ollama, answering questions about the "Attention Is All You Need" paper.
#  RAG Chatbot – Document-Based QA (Local LLM)

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built for learning purposes.

It allows users to ask questions about the paper:
**"Attention Is All You Need" (2017)** — the original Transformer architecture paper.

The chatbot retrieves relevant parts of the document and generates answers using a locally running LLM (no external API calls).

---

## 🧠 Architecture

This project implements a basic RAG pipeline:

1. Load and parse the PDF document.
2. Split the document into smaller chunks.
3. Generate embeddings using Hugging Face models.
4. Store embeddings in a vector database.
5. Retrieve the most relevant chunks based on user queries.
6. Generate answers using LLaMA 3 running locally via Ollama.

---

## 🛠️ Technologies Used

- Python
- Hugging Face (Embeddings)
- Ollama (Local LLaMA 3 model)
- Vector Store ( ChromaDB )
- PDF processing library

---

## 🔐 Why Local LLM?

The model runs locally using Ollama, which means:

- No external API dependency
- No API key required
- Full control over inference
- Good for learning LLM architecture
- More privacy

---

## 📂 Project Structure
rag-chatbot/
│
├── main.py
├── data/
│ └── attention_is_all_you_need.pdf
├── vector_store/
├── requirements.txt
└── README.md




## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sanalayouni/Attention-RAG.git
cd RAG chatbot
---
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
###3️⃣ Install dependencies
```bash
pip install -r requirements.txt
###4️⃣ Install and Run Ollama
Download Ollama from:
https://ollama.com

Pull LLaMA 3 model:
ollama pull llama3

Make sure Ollama is running locally before starting the chatbot.

Run the Application:
```bash
python chatbot.py

Then start asking questions about the paper.

Example:
What is the main idea behind self-attention?
Why are positional encodings necessary?

###🎯 Features

Document-based question answering

Local LLM (LLaMA 3)

Semantic search using embeddings

Lightweight and simple RAG pipeline

No external API usage

###📚 Learning Goals

This project helped me understand:

RAG architecture

Embeddings and vector similarity search

Transformer fundamentals

Running LLMs locally with Ollama

Building AI systems without cloud APIs

###🔮 Future Improvements

Support multiple documents

Add conversational memory

Add Streamlit web interface

Dockerize the application

Add evaluation metrics

###👩‍💻 Author

Sana Layouni
Software Engineering Student
