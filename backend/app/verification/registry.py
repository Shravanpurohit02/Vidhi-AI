from __future__ import annotations

from app.verification.check import VerificationCheck


class VerificationRegistry:

    def __init__(self):
        self._checks:list[VerificationCheck]=[]

    def register(self,check:VerificationCheck):
        self._checks.append(check)

    def checks(self):
        return list(self._checks)
