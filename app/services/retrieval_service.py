from app.services.vector_store_service import VectorStoreService


class RetrievalService:

    def __init__(self):

        self.vector_store = VectorStoreService()

    def retrieve(self, question):

        return self.vector_store.similarity_search(
            question,
            k=5
        )