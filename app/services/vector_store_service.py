from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from app.core.config import settings

class VectorStoreService:

    def __init__(self):

        self.embeddings = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL
        )

        self.db = Chroma(
            collection_name="enterprise_documents",
            embedding_function=self.embeddings,
            persist_directory=settings.CHROMA_PATH
        )

    def add_documents(self, documents, ids):

        self.db.add_documents(
                    documents,
                    ids=ids
                )
    def delete_document(self, filename: str):
        self.db.delete(
        where={
            "file": filename
        }
    )
    def similarity_search(self, question, k=5):

        return self.db.similarity_search(
            question,
            k=k
        )