from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, Field


class TokenUsageMetrics(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ProviderMetrics(BaseModel):
    provider: str
    model: str
    requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_latency_ms: float = 0.0
    tokens: TokenUsageMetrics = Field(default_factory=TokenUsageMetrics)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
