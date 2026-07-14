from __future__ import annotations

from app.ai.services.ai_service import AIService
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class RAGIntegrationCheck(VerificationCheck):

    @property
    def name(self):
        return "RAG Integration"

    def run(self):

        try:

            ai = AIService()

            response = ai.ask("What is Article 21?")

            passed = (
                isinstance(response, dict)
                and "answer" in response
                and "citations" in response
            )

            return VerificationResult(
                name=self.name,
                passed=passed,
                details=f"Citations: {len(response.get('citations', []))}",
            )

        except Exception as exc:
            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
