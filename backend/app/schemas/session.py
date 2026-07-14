from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SessionBase(BaseModel):
    jti: str = Field(..., min_length=1)
    user_id: int


class SessionCreate(SessionBase):
    expires_at: datetime
    user_agent: str | None = None
    ip_address: str | None = None


class SessionResponse(SessionBase):
    issued_at: datetime
    expires_at: datetime
    revoked_at: datetime | None = None
    replaced_by_jti: str | None = None
    user_agent: str | None = None
    ip_address: str | None = None

    model_config = ConfigDict(from_attributes=True)


class SessionRevokeRequest(BaseModel):
    jti: str


class SessionListResponse(BaseModel):
    sessions: list[SessionResponse]
