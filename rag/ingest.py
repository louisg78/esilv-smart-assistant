from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


loader = TextLoader("data/esilv.txt", encoding="utf-8")
docs = loader.load()

embeddings = OllamaEmbeddings(model="tinyllama")
vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="rag/db"
)

print("ESILV knowledge base ingested successfully")
