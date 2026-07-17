from fastapi import APIRouter

from app.models.request_models import AskRequest
from app.models.response_models import AskResponse
from app.services.ollama_service import OllamaService

router = APIRouter(
    prefix="/ask",
    tags=["Ask"]
)

ollama = OllamaService()


@router.post("", response_model=AskResponse)
def ask(request: AskRequest):

    answer = ollama.ask(request.question)

    return AskResponse(
        answer=answer
    )