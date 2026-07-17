from fastapi import APIRouter

from app.models.request_models import AskRequest
from app.models.response_models import AskResponse, Source
from app.services.rag_service import RagService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

rag_service = RagService()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):

    result = rag_service.ask(request.question)

    return AskResponse(
        answer=result["answer"],
        sources=[
            Source(
                file=source["file"],
                page=source["page"]
            )
            for source in result["sources"]
        ]
    )