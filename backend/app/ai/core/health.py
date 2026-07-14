from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, Field


class ProviderHealth(BaseModel):
    provider: str
    healthy: bool
    latency_ms: float = Field(default=0.0, ge=0)
    checked_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    message: str = ""
