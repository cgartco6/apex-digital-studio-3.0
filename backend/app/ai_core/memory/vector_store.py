import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("agent_memory")
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def add(self, text: str, meta: dict):
        embedding = self.embedder.encode(text).tolist()
        self.collection.add(documents=[text], embeddings=[embedding], metadatas=[meta], ids=[meta.get("id")])

    def search(self, query: str):
        embedding = self.embedder.encode(query).tolist()
        return self.collection.query(query_embeddings=[embedding], n_results=3)
