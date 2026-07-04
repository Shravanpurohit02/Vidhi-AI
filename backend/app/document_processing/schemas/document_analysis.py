from datetime import datetime

from pydantic import BaseModel


class DocumentAnalysis(BaseModel):
    document_id: int

    status: str

    document_type: str = ""

    summary: str = ""

    extracted_text: str = ""

    entities: dict = {}

    citations: list[str] = []

    indexed: bool = False

    processed_at: datetime
