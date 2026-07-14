from __future__ import annotations

import uuid

from app.evidence.hashing.hash_service import HashService
from app.evidence.repositories.evidence_repository import EvidenceRepository
from app.evidence.timeline.timeline_service import TimelineService


class EvidenceService:

    def __init__(self):
        self.repository = EvidenceRepository()
        self.timeline = TimelineService()
        self.hash = HashService()

    def register(
        self,
        file_path: str,
        metadata: dict,
    ) -> dict:

        evidence_id = str(uuid.uuid4())

        record = {
            "id": evidence_id,
            "checksum": self.hash.calculate(file_path),
            "metadata": metadata,
            "timeline": [
                self.timeline.event(
                    "system",
                    "registered",
                )
            ],
        }

        self.repository.save(
            evidence_id,
            record,
        )

        return record
