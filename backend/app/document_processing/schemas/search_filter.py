from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class SearchFilter(BaseModel):

    court: str | None = None
    judge: str | None = None
    year: int | None = None
    jurisdiction: str | None = None
    case_type: str | None = None
    act: str | None = None
    section: str | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)
