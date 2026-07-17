from app.core.config import settings
from langchain_core.documents import Document


from app.services.chunk_service import ChunkService
from app.services.document_service import PdfService
from app.services.vector_store_service import VectorStoreService



class IndexingService:

    def __init__(self):
        self.pdf_service = PdfService()
        self.chunk_service = ChunkService()
        self.vector_store = VectorStoreService()

    def ingest(self):

         # Read PDFs
        documents = self.pdf_service.read_pdfs(settings.PDF_FOLDER)

        # Split into chunks
       # Split into chunks
        chunks = self.chunk_service.split_documents(documents)

        # Convert to LangChain Documents
        langchain_documents = []
        ids = []
        for chunk in chunks:
            ids.append(chunk["id"])
            langchain_documents.append(
                Document(
                    page_content=chunk["text"],
                    metadata={
                        "file": chunk["file"],
                        "page": chunk["page"],
                        "chunk": chunk["chunk"]
                    }
                )
            )

        # Store in ChromaDB
        self.vector_store.add_documents(
            langchain_documents,
            ids
        )

        return {
            "documents": len(documents),
            "chunks": len(langchain_documents)
        }
    
    def ingest_single_document(self, file_path: str):

        documents = self.pdf_service.read_pdf(file_path)

        chunks = self.chunk_service.split_documents(documents)

        # Convert chunks to LangChain Documents
        # Store only these chunks in ChromaDB

        return len(chunks)