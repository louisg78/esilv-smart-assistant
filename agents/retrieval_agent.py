from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

# Load once
embeddings = OllamaEmbeddings(model="tinyllama")
db = Chroma(
    persist_directory="rag/db",
    embedding_function=embeddings
)

llm = Ollama(model="tinyllama")

def retrieve_answer(query):
    docs = db.similarity_search(query, k=2)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an official ESILV assistant.
Use ONLY the information below.
If the answer is not present, say you do not know.

Context:
{context}

Question:
{query}
"""

    return llm.invoke(prompt)
