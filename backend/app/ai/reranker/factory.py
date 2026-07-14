from __future__ import annotations

from app.ai.reranker.service import RerankerService


def build_reranker():
    return RerankerService()
