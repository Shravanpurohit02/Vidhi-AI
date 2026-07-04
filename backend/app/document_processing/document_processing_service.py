from datetime import UTC, datetime

from app.ai.services.ai_service import AIService
from app.legal.citations.extractor import CitationExtractor
from app.legal.entities.entity_extractor import LegalEntityExtractor
from app.legal.reasoning.summarizer import JudgmentSummarizer
from app.document_processing.schemas.document_analysis import (
    DocumentAnalysis,
)


class DocumentProcessingService:

    def __init__(self):
        self.ai = AIService()
        self.entities = LegalEntityExtractor()
        self.citations = CitationExtractor()
        self.summarizer = JudgmentSummarizer()

    def process(
        self,
        document_id: int,
        text: str,
    ) -> DocumentAnalysis:

        cleaned = text.strip()

        summary = self.summarizer.summarize(cleaned)

        entity_data = self.entities.extract(cleaned)

        citation_data = self.citations.extract(cleaned)

        self.ai.ingest_document(
            cleaned,
            {
                "document_id": document_id,
            },
        )

        return DocumentAnalysis(
            document_id=document_id,
            status="processed",
            document_type="legal_document",
            summary=summary,
            extracted_text=cleaned,
            entities=entity_data,
            citations=citation_data,
            indexed=True,
            processed_at=datetime.now(UTC),
        )
