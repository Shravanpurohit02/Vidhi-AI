from __future__ import annotations

from app.document_processing.document_processing_service import DocumentProcessingService
from app.verification.check import VerificationCheck
from app.verification.result import VerificationResult


class DocumentProcessingCheck(VerificationCheck):

    @property
    def name(self):
        return "Document Processing"

    def run(self):

        try:

            service = DocumentProcessingService()

            result = service.process(
                document_id=0,
                text="The Supreme Court interpreted Article 21 of the Constitution of India."
            )

            return VerificationResult(
                name=self.name,
                passed=result.indexed,
                details=f"Status={result.status}, Indexed={result.indexed}"
            )

        except Exception as exc:

            return VerificationResult(
                name=self.name,
                passed=False,
                details=f"{type(exc).__name__}: {exc}"
            )
