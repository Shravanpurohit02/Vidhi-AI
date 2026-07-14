from __future__ import annotations

import importlib

from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


MODULES = [
    "app.main",
    "app.ai.services.ai_service",
    "app.ai.retrieval.search",
    "app.document_processing.document_processing_service",
    "app.ai.vectorstore.service",
]


class ImportCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "Import Verification"

    def run(self) -> VerificationResult:

        failures = []

        for module in MODULES:
            try:
                importlib.import_module(module)
            except Exception as exc:
                failures.append(f"{module}: {exc}")

        return VerificationResult(
            name=self.name,
            passed=not failures,
            details="\n".join(failures) if failures else "All imports succeeded",
        )
