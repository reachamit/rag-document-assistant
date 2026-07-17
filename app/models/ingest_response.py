from pydantic import BaseModel


class IngestResponse(BaseModel):
    success: bool
    documents: int
    chunks: int
    message: str