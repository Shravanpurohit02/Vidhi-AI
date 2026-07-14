from datetime import datetime

from pydantic import BaseModel, Field


class Citation(BaseModel):
    title: str

    citation: str = ""

    court: str = ""

    year: int | None = None

    judge: str = ""

    bench: str = ""

    paragraphs: list[int] = Field(default_factory=list)

    document_id: str = ""

    source: str = ""

    url: str = ""

    score: float = 0.0


class ResearchResponse(BaseModel):
    session_id: str

    question: str

    answer: str

    summary: str

    entities: dict = Field(default_factory=dict)

    contexts_found: int = 0

    citations: list[Citation] = Field(default_factory=list)

    sources: list[str] = Field(default_factory=list)

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    provider: str = ""

    model: str = ""

    processing_time: float = 0.0

    created_at: datetime
