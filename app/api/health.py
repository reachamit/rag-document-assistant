from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get(
    "",
    summary="Application Health",
    description="Returns API health status."
)
def health():

    return {
        "status": "Healthy"
    }