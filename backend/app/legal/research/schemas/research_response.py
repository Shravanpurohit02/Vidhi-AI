from datetime import datetime

from pydantic import BaseModel, Field


class Citation(BaseModel):
    title: str
    source: str


class ResearchResponse(BaseModel):
    session_id: str

    question: str

    answer: str

    summary: str

    entities: dict = {}

    contexts_found: int = 0

    citations: list[Citation] = []

    sources: list[str] = []

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    provider: str = ""

    model: str = ""

    processing_time: float = 0.0

    created_at: datetime
