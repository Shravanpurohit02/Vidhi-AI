from datetime import datetime

from pydantic import BaseModel


class ReasoningResponse(BaseModel):
    answer: str

    reasoning: str

    citations: list[str] = []

    provider: str = ""

    model: str = ""

    processing_time: float = 0.0

    generated_at: datetime
