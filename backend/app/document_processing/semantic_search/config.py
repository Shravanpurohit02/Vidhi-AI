from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SemanticSearchConfig:
    default_top_k: int = 5
    rerank: bool = True
    query_expansion: bool = True
