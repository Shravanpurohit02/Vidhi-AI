from __future__ import annotations

from app.ai.cache.embedding_cache import EmbeddingCache
from app.ai.embeddings.embedding_selector import selector
from app.ai.storage.vector_store import PersistentVectorStore


class IndexManager:

    def __init__(self):

        self.embedder = selector.select()
        self.store = PersistentVectorStore()
        self.cache = EmbeddingCache()

    def _embedding(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.cache.get(text)

        if embedding is None:
            embedding = self.embedder.create(text)
            self.cache.put(
                text,
                embedding,
            )

        return embedding

    def index(
        self,
        text: str,
        metadata: dict,
    ) -> None:

        self.store.add(
            text,
            metadata,
            self._embedding(text),
        )

    def index_many(
        self,
        documents: list[tuple[str, dict]],
    ) -> None:

        for text, metadata in documents:
            self.index(
                text,
                metadata,
            )

    def stats(self) -> dict[str, int]:

        return {
            "documents": self.store.count(),
            "cached_embeddings": len(self.cache.cache),
        }

    def clear_cache(self) -> None:

        self.cache.cache.clear()

    def clear_index(self) -> None:

        self.store.clear()
