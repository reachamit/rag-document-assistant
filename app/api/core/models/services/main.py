from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Document RAG API",
    version="1.0.0",
    description="RAG API using Ollama + ChromaDB"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Document RAG API is running"
    }