from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field
from app.document_processing.schemas.search_filter import SearchFilter


class VectorRecord(BaseModel):
    document_id: int
    chunk_id: int
    provider: str
    model: str
    dimensions: int = Field(gt=0)
    vector: list[float] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class VectorSearchRequest(BaseModel):
    query_vector: list[float]
    top_k: int = Field(default=5, ge=1)
    provider: str | None = None
    filters: SearchFilter = Field(default_factory=SearchFilter)


class VectorSearchResult(BaseModel):
    document_id: int
    chunk_id: int
    score: float
    vector: list[float] | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
