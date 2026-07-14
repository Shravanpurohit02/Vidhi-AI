from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256


@dataclass(slots=True)
class ChunkMetadata:
    document_id: str | None
    chunk_index: int
    total_chunks: int
    character_count: int
    token_estimate: int
    checksum: str

    @classmethod
    def build(
        cls,
        text: str,
        chunk_index: int,
        total_chunks: int,
        document_id: str | None = None,
    ) -> "ChunkMetadata":
        return cls(
            document_id=document_id,
            chunk_index=chunk_index,
            total_chunks=total_chunks,
            character_count=len(text),
            token_estimate=len(text.split()),
            checksum=sha256(text.encode("utf-8")).hexdigest(),
        )
