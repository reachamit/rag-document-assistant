from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    APP_NAME = "RAG Assistant"

    VERSION = "1.0.0"

    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    CHROMA_PATH = os.getenv("CHROMA_PATH")

    PDF_FOLDER = os.getenv("PDF_FOLDER")


settings = Settings()