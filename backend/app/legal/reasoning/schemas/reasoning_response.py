from datetime import datetime

from pydantic import BaseModel, Field


class ReasoningResponse(BaseModel):
    answer: str

    reasoning: str

    citations: list[str] = Field(default_factory=list)

    confidence: float = 0.0

    reasoning_strategy: str = "general_analysis"

    explainability_score: float = 0.0

    citation_support: int = 0

    provider: str = ""

    model: str = ""

    processing_time: float = 0.0

    generated_at: datetime
