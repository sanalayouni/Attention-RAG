from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import gradio as gr

# configuration
CHROMA_PATH = "chroma_db"

# 🔹 Local Embeddings (FREE)
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 🔹 Local LLM from Ollama (FREE)
llm = Ollama(
    model="llama3",  # make sure this model is installed in ollama
    temperature=0.5
)

# connect to chromadb
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH,
)

# retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 5})


def stream_response(message, history):

    # retrieve relevant docs
    docs = retriever.invoke(message)

    knowledge = ""
    for doc in docs:
        knowledge += doc.page_content + "\n\n"

    rag_prompt = f"""
You are an assistant that answers questions only using the provided knowledge.

Question:
{message}

Conversation history:
{history}

Knowledge:
{knowledge}
"""

    partial_message = ""

    # Ollama streaming
    for chunk in llm.stream(rag_prompt):
        partial_message += chunk
        yield partial_message


# Gradio UI
chatbot = gr.ChatInterface(
    stream_response,
    textbox=gr.Textbox(
        placeholder="Send your question...",
        container=False,
        autoscroll=True,
        scale=7,
    ),
)

chatbot.launch()