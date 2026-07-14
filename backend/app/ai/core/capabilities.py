from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Capability(str, Enum):
    CHAT = "chat"
    STREAMING = "streaming"
    EMBEDDINGS = "embeddings"
    RERANKING = "reranking"
    TOOLS = "tools"
    JSON_MODE = "json_mode"
    VISION = "vision"


class ProviderCapabilities(BaseModel):
    chat: bool = True
    streaming: bool = False
    embeddings: bool = False
    reranking: bool = False
    tools: bool = False
    json_mode: bool = False
    vision: bool = False

    max_context_tokens: int = Field(default=0, ge=0)
    max_output_tokens: int = Field(default=0, ge=0)
