from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SearchResult:
    document_id: str
    chunk_id: str
    score: float
    text: str
    metadata: dict
