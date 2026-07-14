from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DraftingConfig:
    default_provider: str = "ollama"
    default_style: str = "formal"
    enable_citations: bool = True
    enable_rag: bool = True
    enable_review: bool = True
    enable_improvements: bool = True
