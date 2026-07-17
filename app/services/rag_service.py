from app.services.ollama_service import OllamaService
from app.services.retrieval_service import RetrievalService


class RagService:

    def __init__(self):
        self.llm = OllamaService()
        self.retriever = RetrievalService()

    def ask(self, question: str):

        documents = self.retriever.retrieve(question)

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

Information not found in the uploaded documents.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = self.llm.ask(prompt)

        sources = []

        for doc in documents:

            sources.append({
                "file": doc.metadata["file"],
                "page": doc.metadata["page"]
            })

        return {
            "answer": answer,
            "sources": sources
        }