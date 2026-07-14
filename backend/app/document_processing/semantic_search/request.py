from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SearchRequest:
    query: str
    top_k: int = 5
    provider: str | None = None
    rerank: bool = True
    filters: dict | None = None
