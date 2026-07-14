from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EvidenceHash:
    algorithm: str
    value: str
