from app.services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

vector = embedding_service.embed_query(
    "What is annual leave?"
)

print(type(vector))
print(len(vector))
print(vector[:10])