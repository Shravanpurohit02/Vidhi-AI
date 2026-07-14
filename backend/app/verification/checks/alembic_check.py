from __future__ import annotations

from sqlalchemy import create_engine, inspect

from app.core.config import settings
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class AlembicCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "Alembic"

    def run(self) -> VerificationResult:

        try:
            engine = create_engine(settings.DATABASE_URL)
            inspector = inspect(engine)

            tables = inspector.get_table_names()

            if "alembic_version" not in tables:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details="alembic_version table not found.",
                )

            with engine.connect() as conn:
                rows = conn.exec_driver_sql(
                    "SELECT version_num FROM alembic_version"
                ).fetchall()

            if len(rows) != 1:
                return VerificationResult(
                    name=self.name,
                    passed=False,
                    details=f"Expected 1 revision, found {len(rows)}.",
                )

            return VerificationResult(
                name=self.name,
                passed=True,
                details=f"Current revision: {rows[0][0]}",
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
