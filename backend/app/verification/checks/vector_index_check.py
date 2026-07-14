from __future__ import annotations

from app.ai.vectorstore.service import VectorStoreService
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class VectorStoreCheck(VerificationCheck):

    @property
    def name(self):
        return "Vector Index"

    def run(self):

        try:

            service = VectorStoreService()

            providers = service.providers()

            if not providers:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="No vector providers registered.",
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details="Providers: " + ", ".join(providers),
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
