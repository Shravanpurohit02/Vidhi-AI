from __future__ import annotations

from app.core.config import settings
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class SecurityCheck(VerificationCheck):

    @property
    def name(self):
        return "Security"

    def run(self):

        try:

            issues = []

            if hasattr(settings, "SECRET_KEY"):

                if len(settings.SECRET_KEY) < 32:
                    issues.append("SECRET_KEY is shorter than 32 characters.")

            if hasattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES"):

                if settings.ACCESS_TOKEN_EXPIRE_MINUTES <= 0:
                    issues.append("Invalid access token expiry.")

            if issues:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="\n".join(issues),
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details="Security configuration validated.",
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
