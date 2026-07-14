from __future__ import annotations

from app.ai.search.hybrid_search import HybridSearch
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class RetrieverCheck(VerificationCheck):

    @property
    def name(self):
        return "Retriever"

    def run(self):

        try:
            search = HybridSearch()

            results = search.search(
                "Supreme Court judgment",
                top_k=3,
            )

            return VerificationResult(
                name=self.name,
                passed=isinstance(results, list),
                details=f"Retrieved {len(results)} result(s).",
            )

        except Exception as exc:
            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}",
            )
