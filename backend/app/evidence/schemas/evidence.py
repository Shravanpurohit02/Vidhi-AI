from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class EvidenceCreate(BaseModel):
    case_id: int | None = None
    title: str
    description: str = ""


class EvidenceResponse(BaseModel):
    id: str
    title: str
    filename: str
    content_type: str
    size: int
    sha256: str
    uploaded_at: datetime
