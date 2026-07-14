from __future__ import annotations

from app.document_processing.chunking.sentence_splitter import SentenceSplitter


class SemanticChunker:
    """
    Semantic chunker.

    v1 groups neighbouring sentences.
    Future versions will use embeddings to detect topic changes.
    """

    def __init__(self, sentences_per_chunk: int = 5):
        self.sentences_per_chunk = sentences_per_chunk

    def chunk(self, text: str) -> list[str]:
        sentences = SentenceSplitter.split(text)

        chunks: list[str] = []

        for i in range(0, len(sentences), self.sentences_per_chunk):
            chunk = " ".join(sentences[i : i + self.sentences_per_chunk])

            if chunk.strip():
                chunks.append(chunk)

        return chunks
