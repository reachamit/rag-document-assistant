from langchain_ollama import ChatOllama

from app.core.config import settings


class OllamaService:

    def __init__(self):
        self.llm = ChatOllama(
            model=settings.OLLAMA_MODEL,
            temperature=0
        )

    def ask(self, question: str):

        response = self.llm.invoke(question)

        return response.content