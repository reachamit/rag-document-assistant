from fastapi import APIRouter

from app.models.ingest_response import IngestResponse
from app.services.indexing_service import IndexingService

router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)

service = IndexingService()


@router.post("", response_model=IngestResponse)
def ingest():

    result = service.ingest()

    return IngestResponse(
        success=True,
        documents=result["documents"],
        chunks=result["chunks"],
        message="Documents indexed successfully."
    )