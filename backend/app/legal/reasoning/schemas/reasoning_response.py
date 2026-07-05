from datetime import datetime

from pydantic import BaseModel, Field


class ReasoningResponse(BaseModel):
    answer: str

    reasoning: str

    citations: list[str] = Field(default_factory=list)

    provider: str = ""

    model: str = ""

    processing_time: float = 0.0

    generated_at: datetime
