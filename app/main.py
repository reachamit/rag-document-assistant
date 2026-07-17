from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.ask import router as ask_router
from app.api.ingest import router as ingest_router
from app.api.rag import router as rag_router
from app.api.documents import router as documents_router

app = FastAPI(
    title="Document RAG API",
    version="1.0.0",
    description="RAG API using Ollama + ChromaDB",
    contact={
        "name": "Your Name",
        "email": "your@email.com"
    }
)

app.include_router(health_router)
app.include_router(ask_router)
app.include_router(ingest_router)
app.include_router(rag_router)
app.include_router(documents_router)

@app.get("/", tags=["Root"])
def root():
    return {
        "application": "RAG Assistant",
        "version": "1.0.0",
        "status": "Running"
    }