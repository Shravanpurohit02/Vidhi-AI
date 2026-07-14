from __future__ import annotations

from app.core.config import settings
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class ConfigurationCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "Configuration"

    def run(self) -> VerificationResult:

        try:

            issues = []

            if not settings.APP_NAME:
                issues.append("APP_NAME is empty.")

            if not settings.APP_VERSION:
                issues.append("APP_VERSION is empty.")

            if not settings.DATABASE_URL:
                issues.append("DATABASE_URL is empty.")

            if hasattr(settings, "SECRET_KEY") and not settings.SECRET_KEY:
                issues.append("SECRET_KEY is empty.")

            if issues:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="\n".join(issues),
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details="Configuration validated successfully.",
            )

        except Exception as exc:
            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
