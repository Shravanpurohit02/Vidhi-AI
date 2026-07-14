from __future__ import annotations

from app.ai.embeddings.embedding_selector import selector

from app.document_processing.schemas.vector import (
    VectorSearchRequest,
)
from app.ai.vectorstore.service import (
    VectorStoreService,
)


class Retriever:
    """
    Read-only retrieval component.

    Responsibilities:
      - Embed user queries.
      - Search the vector index.
      - Return ranked results.

    Document ingestion is handled by:
      DocumentProcessingService ->
      DocumentChunkService ->
      EmbeddingIngestionService
    """

    def __init__(self):
        self.embedder = selector.select()
        self.index = VectorStoreService()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        provider: str | None = None,
    ):
        vector = self.embedder.create(query)

        request = VectorSearchRequest(
            query_vector=vector,
            top_k=top_k,
            provider=provider,
        )

        return self.index.search(request)
