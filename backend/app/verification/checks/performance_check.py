from __future__ import annotations

import time

from app.ai.search.hybrid_search import HybridSearch
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class PerformanceCheck(VerificationCheck):

    @property
    def name(self):
        return "Performance"

    def run(self):

        try:

            search = HybridSearch()

            started = time.perf_counter()

            search.search(
                "Article 21 Constitution of India",
                top_k=5,
            )

            elapsed = (time.perf_counter() - started) * 1000

            return VerificationResult(
                name=self.name,
                passed=True,
                details=f"Retrieval latency: {elapsed:.2f} ms",
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
