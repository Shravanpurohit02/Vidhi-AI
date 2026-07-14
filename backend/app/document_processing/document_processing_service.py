from datetime import UTC, datetime

from app.document_processing.chunking.document_chunk_service import (
    DocumentChunkService,
)
from app.ai.embeddings.embedding_ingestion_service import (
    EmbeddingIngestionService,
)
from app.document_processing.schemas.document_analysis import (
    DocumentAnalysis,
)
from app.legal.citations.extractor import CitationExtractor
from app.legal.entities.entity_extractor import LegalEntityExtractor
from app.legal.reasoning.summarizer import JudgmentSummarizer


class DocumentProcessingService:

    def __init__(self):
        self.chunk_service = DocumentChunkService()
        self.embedding_service = EmbeddingIngestionService()
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

        chunks = self.chunk_service.create_chunks(
            document_id=document_id,
            text=cleaned,
        )

        self.embedding_service.ingest(chunks)

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
