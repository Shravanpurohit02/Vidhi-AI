from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AIIntegrationConfig:
    default_provider: str = "ollama"
    default_model: str = ""
    temperature: float = 0.2
    max_tokens: int = 4096
    enable_rag: bool = True
    enable_tools: bool = True
    enable_streaming: bool = True
    enable_memory: bool = True
    enable_citations: bool = True
