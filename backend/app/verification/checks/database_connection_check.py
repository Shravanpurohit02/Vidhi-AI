from __future__ import annotations

from sqlalchemy import text

from app.database.database import SessionLocal
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class DatabaseConnectionCheck(VerificationCheck):

    @property
    def name(self):
        return "Database Connection"

    def run(self):

        db = SessionLocal()

        try:

            db.execute(text("SELECT 1"))

            return VerificationResult(
                name=self.name,
                passed=True,
                details="Database connection successful.",
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )

        finally:
            db.close()
