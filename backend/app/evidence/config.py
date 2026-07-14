from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EvidenceConfig:
    storage_provider: str = "local"
    hash_algorithm: str = "sha256"
    verify_on_upload: bool = True
    enable_chain_of_custody: bool = True
    enable_versioning: bool = True
