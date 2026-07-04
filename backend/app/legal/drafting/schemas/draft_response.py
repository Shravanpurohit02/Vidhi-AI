from datetime import datetime

from pydantic import BaseModel


class DraftResponse(BaseModel):
    template: str
    document: str

    provider: str = ""
    model: str = ""

    processing_time: float = 0.0

    word_count: int = 0

    generated_at: datetime
