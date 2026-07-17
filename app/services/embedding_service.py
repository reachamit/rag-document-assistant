from langchain_ollama import OllamaEmbeddings

from app.core.config import settings


class EmbeddingService:

    def __init__(self):
        self.embedding = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL
        )

    def embed_documents(self, texts):
        return self.embedding.embed_documents(texts)

    def embed_query(self, question):
        return self.embedding.embed_query(question)