from __future__ import annotations

from app.main import app
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class RouteCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "API Routes"

    def run(self) -> VerificationResult:

        try:
            routes = sorted(
                f"{','.join(sorted(r.methods))} {r.path}"
                for r in app.routes
                if hasattr(r, "methods")
            )

            return VerificationResult(
                name=self.name,
                passed=True,
                details="\n".join(routes),
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
