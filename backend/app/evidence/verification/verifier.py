from __future__ import annotations

from app.evidence.hashing.hash_service import HashService


class EvidenceVerifier:

    def __init__(self):
        self.hash = HashService()

    def verify(
        self,
        path: str,
        expected: str,
    ) -> bool:

        return self.hash.calculate(path) == expected
