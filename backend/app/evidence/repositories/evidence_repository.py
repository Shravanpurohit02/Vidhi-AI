from __future__ import annotations


class EvidenceRepository:

    def __init__(self):
        self._records: dict[str, dict] = {}

    def save(
        self,
        evidence_id: str,
        data: dict,
    ) -> None:
        self._records[evidence_id] = data

    def get(
        self,
        evidence_id: str,
    ) -> dict | None:
        return self._records.get(evidence_id)

    def delete(
        self,
        evidence_id: str,
    ) -> None:
        self._records.pop(evidence_id, None)
