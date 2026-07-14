from __future__ import annotations

import importlib

from app.database.database import Base
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class ModelCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "SQLAlchemy Models"

    def run(self) -> VerificationResult:

        try:
            import app.models

            tables = sorted(Base.metadata.tables.keys())

            if not tables:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="No SQLAlchemy tables registered.",
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details="Registered tables:\n" + "\n".join(tables),
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
