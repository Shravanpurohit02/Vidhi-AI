from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class VerificationResult:
    name: str
    passed: bool
    details: str = ""
    duration: float = 0.0
