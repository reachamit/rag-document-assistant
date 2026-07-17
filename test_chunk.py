from app.services.document_service import PdfService
from app.services.chunk_service import ChunkService
from app.core.config import settings

pdf = PdfService()

documents = pdf.read_pdfs(
    settings.PDF_FOLDER
)

chunk_service = ChunkService()

chunks = chunk_service.split_documents(
    documents
)

print(f"Total Chunks : {len(chunks)}")

for chunk in chunks:
    print(chunk)