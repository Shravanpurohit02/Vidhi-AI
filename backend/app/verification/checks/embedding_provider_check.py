from __future__ import annotations

from app.ai.embeddings.service import EmbeddingService
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class EmbeddingProviderCheck(VerificationCheck):

    @property
    def name(self):
        return "Embedding Provider"

    def run(self):

        try:

            service = EmbeddingService()

            providers = service.providers()

            if not providers:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="No embedding providers available.",
                )

            result = service.embed("Vidhi AI verification")

            vector = result.get("vector")

            if not isinstance(vector, list):
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="Provider did not return a vector list.",
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details=(
                    f"Providers: {', '.join(providers)}\n"
                    f"Dimensions: {len(vector)}"
                ),
            )

        except Exception as exc:
            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
