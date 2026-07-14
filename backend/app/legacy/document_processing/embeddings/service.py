from __future__ import annotations

from app.document_processing.embeddings.adapter import EmbeddingAdapter
from app.document_processing.embeddings.bootstrap import build_registry


class EmbeddingService:

    def __init__(self):
        self.registry = build_registry()
        self.adapter = EmbeddingAdapter(self.registry)

    def embed(
        self,
        text: str,
        provider: str | None = None,
    ) -> dict:
        return self.adapter.embed(text, provider)

    def embed_batch(
        self,
        texts: list[str],
        provider: str | None = None,
    ) -> dict:
        return self.adapter.embed_batch(texts, provider)

    def providers(self) -> list[str]:
        return self.registry.available()

    def all_providers(self) -> list[str]:
        return self.registry.all()
