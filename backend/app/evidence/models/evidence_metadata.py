from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class EvidenceMetadata:
    id: str
    filename: str
    content_type: str
    size: int
    uploaded_at: datetime
