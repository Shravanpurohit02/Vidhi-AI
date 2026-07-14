from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class AIRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    system_prompt: str | None = None
    model: str | None = None
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int | None = Field(default=None, gt=0)
    top_p: float = Field(default=1.0, gt=0.0, le=1.0)
    stream: bool = False
    json_mode: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)
