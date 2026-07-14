from __future__ import annotations

from app.document_processing.chunking.text_cleaner import TextCleaner
from app.document_processing.chunking.token_chunker import TokenChunker
from app.document_processing.chunking.semantic_chunker import SemanticChunker
from app.document_processing.chunking.chunk_metadata import ChunkMetadata


class ChunkPipeline:
    """
    End-to-end chunking pipeline.
    """

    def __init__(
        self,
        strategy: str = "token",
        chunk_size: int = 512,
        overlap: int = 64,
    ):
        self.strategy = strategy

        self.token_chunker = TokenChunker(
            chunk_size=chunk_size,
            overlap=overlap,
        )

        self.semantic_chunker = SemanticChunker()

    def process(
        self,
        text: str,
        document_id: str | None = None,
    ) -> list[dict]:

        cleaned = TextCleaner.clean(text)

        if self.strategy == "semantic":
            chunks = self.semantic_chunker.chunk(cleaned)
        else:
            chunks = self.token_chunker.chunk(cleaned)

        total = len(chunks)

        results = []

        for index, chunk in enumerate(chunks):

            metadata = ChunkMetadata.build(
                text=chunk,
                chunk_index=index,
                total_chunks=total,
                document_id=document_id,
            )

            results.append(
                {
                    "text": chunk,
                    "metadata": metadata.__dict__,
                }
            )

        return results
