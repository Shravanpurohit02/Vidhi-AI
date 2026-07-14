from __future__ import annotations

from app.evidence.hashing.checksum import sha256


class HashService:

    def calculate(
        self,
        path: str,
    ) -> str:
        return sha256(path)
