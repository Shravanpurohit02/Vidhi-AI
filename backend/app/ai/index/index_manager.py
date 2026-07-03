from app.ai.cache.embedding_cache import EmbeddingCache
from app.ai.embeddings.mock import MockEmbeddingProvider
from app.ai.storage.vector_store import PersistentVectorStore


class IndexManager:

    def __init__(self):

        self.embedder = MockEmbeddingProvider()
        self.store = PersistentVectorStore()
        self.cache = EmbeddingCache()

    def index(
        self,
        text,
        metadata,
    ):

        embedding = self.cache.get(text)

        if embedding is None:

            embedding = self.embedder.embed(text)

            self.cache.put(
                text,
                embedding,
            )

        self.store.add(
            text,
            metadata,
            embedding,
        )
