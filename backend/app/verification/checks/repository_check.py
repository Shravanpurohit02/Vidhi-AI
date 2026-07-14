from __future__ import annotations

import importlib
from pathlib import Path

from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class RepositoryCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "Repositories"

    def run(self) -> VerificationResult:

        failures = []

        root = Path("app")

        for file in root.rglob("*repository.py"):

            module = (
                str(file.with_suffix(""))
                .replace("/", ".")
                .replace("\\", ".")
            )

            try:
                importlib.import_module(module)

            except Exception as exc:
                failures.append(f"{module}: {type(exc).__name__}: {exc}")

        if failures:
            return VerificationResult(
                name=self.name,
                passed=False,
                details="\n".join(failures),
            )

        return VerificationResult(
            name=self.name,
            passed=True,
            details="All repository modules imported successfully.",
        )
