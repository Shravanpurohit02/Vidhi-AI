from __future__ import annotations

from app.evidence.verification.verifier import EvidenceVerifier


class IntegrityChecker:

    def __init__(self):
        self.verifier = EvidenceVerifier()

    def check(
        self,
        path: str,
        checksum: str,
    ) -> bool:

        return self.verifier.verify(path, checksum)
