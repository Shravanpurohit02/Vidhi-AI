from __future__ import annotations

from .retriever import Retriever
from app.ai.search.hybrid_search import HybridSearch

__all__ = ["Retriever", "HybridSearch", "Search"]


class Search(HybridSearch):
    """Backward-compatible alias."""
    pass
