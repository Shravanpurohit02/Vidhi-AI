from __future__ import annotations

from app.document_processing.chunking.sentence_splitter import SentenceSplitter


class TokenChunker:
    """
    Simple token-aware chunker.

    Uses word count as an approximation so it remains
    model-independent.
    """

    def __init__(
        self,
        chunk_size: int = 512,
        overlap: int = 64,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> list[str]:
        sentences = SentenceSplitter.split(text)

        chunks: list[str] = []

        current: list[str] = []
        current_tokens = 0

        for sentence in sentences:
            token_count = len(sentence.split())

            if current and current_tokens + token_count > self.chunk_size:
                chunks.append(" ".join(current))

                overlap_words = " ".join(current).split()
                overlap_words = overlap_words[-self.overlap :]

                current = [" ".join(overlap_words)]
                current_tokens = len(overlap_words)

            current.append(sentence)
            current_tokens += token_count

        if current:
            chunks.append(" ".join(current))

        return chunks
