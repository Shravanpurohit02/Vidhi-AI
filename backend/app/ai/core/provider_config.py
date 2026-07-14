from __future__ import annotations

from pydantic import BaseModel, Field


class ProviderConfig(BaseModel):
    name: str
    enabled: bool = True
    priority: int = 100
    timeout: float = Field(default=60.0, gt=0)
    max_retries: int = Field(default=3, ge=0)
    api_key_env: str | None = None
    model: str | None = None
    base_url: str | None = None
