from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.core.config import settings
from app.models.response_models import ApiResponse
from app.services.indexing_service import IndexingService
from app.services.vector_store_service import VectorStoreService
router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

indexing_service = IndexingService()


@router.get("")
def get_documents():

    folder = Path(settings.PDF_FOLDER)

    documents = []

    for pdf in folder.glob("*.pdf"):

        documents.append(
            {
                "name": pdf.name,
                "size_kb": round(pdf.stat().st_size / 1024, 2)
            }
        )

    return documents


@router.post("/upload", response_model=ApiResponse)
def upload_document(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    destination = Path(settings.PDF_FOLDER) / file.filename

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Auto Index
    #indexing_service.ingest() Issue will rise for more than 10000 files 
    indexing_service.ingest_single_document(destination)

    return ApiResponse(
        success=True,
        message="Document uploaded and indexed successfully."
    )


@router.delete("/{filename}", response_model=ApiResponse)
def delete_document(filename: str):

    file_path = Path(settings.PDF_FOLDER) / filename

    if not file_path.exists():

        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    file_path.unlink()
    VectorStoreService.delete_document(filename)
    # Version 2.1
    # Remove vectors from ChromaDB

    return ApiResponse(
        success=True,
        message="Document deleted successfully."
    )