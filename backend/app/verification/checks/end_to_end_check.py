from __future__ import annotations

from app.ai.services.ai_service import AIService
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class EndToEndCheck(VerificationCheck):

    @property
    def name(self):
        return "End-to-End"

    def run(self):

        try:

            ai = AIService()

            response = ai.ask(
                "What is Article 21?"
            )

            if not isinstance(response, dict):
                return VerificationResult(
                    self.name,
                    False,
                    "AIService returned an invalid response."
                )

            required = {
                "answer",
                "provider",
                "model",
                "citations",
            }

            missing = required - set(response.keys())

            if missing:
                return VerificationResult(
                    self.name,
                    False,
                    f"Missing keys: {sorted(missing)}"
                )

            return VerificationResult(
                self.name,
                True,
                "End-to-end AI pipeline operational."
            )

        except Exception as exc:

            return VerificationResult(
                self.name,
                False,
                f"{type(exc).__name__}: {exc}"
            )
