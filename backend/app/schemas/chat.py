from __future__ import annotations

from pydantic import BaseModel


class ChatRequest(BaseModel):
    conversation_id: str
    message: str
    provider: str | None = None


class ChatResponse(BaseModel):
    response: str
    citations: str
