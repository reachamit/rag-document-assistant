from app.services.document_service import PdfService
from app.core.config import settings

pdf = PdfService()

docs = pdf.read_pdfs(settings.PDF_FOLDER)

print(docs[:3])