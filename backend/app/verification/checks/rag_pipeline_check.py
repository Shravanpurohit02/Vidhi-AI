from __future__ import annotations

from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class RAGPipelineCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "RAG Pipeline"

    def run(self) -> VerificationResult:

        try:
            from app.ai.chunking.chunker import TextChunker
            from app.ai.embeddings.service import EmbeddingService
            from app.ai.vectorstore.service import VectorStoreService

            chunker = TextChunker()
            chunks = chunker.chunk(
                "The Supreme Court of India delivered a landmark constitutional judgment."
            )

            if not chunks:
                return VerificationResult(
                    self.name,
                    False,
                    "Chunker returned no chunks."
                )

            embedding_service = EmbeddingService()

            try:
                vector = embedding_service.embed(chunks[0])
            except Exception as exc:
                return VerificationResult(
                    self.name,
                    False,
                    f"Embedding generation failed: {exc}"
                )

            index = VectorStoreService()

            providers = index.providers()

            return VerificationResult(
                self.name,
                True,
                f"Chunks: {len(chunks)}\nProviders: {providers}"
            )

        except Exception as exc:
            return VerificationResult(
                self.name,
                False,
                f"{type(exc).__name__}: {exc}"
            )
