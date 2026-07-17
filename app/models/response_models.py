from pydantic import BaseModel


from pydantic import BaseModel


class Source(BaseModel):
    file: str
    page: int


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]


class ApiResponse(BaseModel):
    success: bool
    message: str