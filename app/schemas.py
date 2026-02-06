from pydantic import BaseModel, Field


class ExplainRequest(BaseModel):
    code: str = Field(..., min_length=1, max_length=12000)


class ExplainResponse(BaseModel):
    language: str
    explanation_markdown: str
