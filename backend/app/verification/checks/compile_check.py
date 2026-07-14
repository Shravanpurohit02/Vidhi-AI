from __future__ import annotations

import compileall

from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class CompileCheck(VerificationCheck):

    @property
    def name(self) -> str:
        return "Compilation"

    def run(self) -> VerificationResult:

        ok = compileall.compile_dir("app", quiet=1)

        return VerificationResult(
            name=self.name,
            passed=ok,
            details="Compilation successful" if ok else "Compilation failed",
        )
