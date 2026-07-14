from datetime import UTC, datetime
from time import perf_counter

from app.ai.services.ai_service import AIService
from app.core.logging import get_logger
from app.legal.drafting.clauses.defaults import load_default_clauses
from app.legal.drafting.clauses.engine import engine
from app.legal.drafting.schemas.draft_response import DraftResponse
from app.legal.templates.templates import TEMPLATES
from app.legal.templates.validator import validator
from app.legal.citations.inserter import inserter as citation_inserter
from app.legal.citations.validator import validator as citation_validator
from app.legal.citations.extractor import CitationExtractor

logger = get_logger()


class DraftingService:

    def __init__(self):
        self.ai = AIService()
        load_default_clauses()
        self.citation_extractor = CitationExtractor()

    def _build_prompt(
        self,
        template: str,
        facts: str,
        relief: str,
    ) -> str:

        validator.validate(template)

        template_text = TEMPLATES[template]

        clause_text = engine.build(
            [
                "heading",
                "facts",
                "relief",
                "signature",
            ],
            facts=facts,
            relief=relief,
        )

        return f"{template_text}\n\n" f"{clause_text}"

    def generate(
        self,
        template: str,
        facts: str,
        relief: str = "",
    ) -> DraftResponse:

        logger.info(f"Draft generation started (template={template})")

        started = perf_counter()

        try:

            prompt = self._build_prompt(
                template,
                facts,
                relief,
            )

            logger.info("Draft prompt constructed.")

            result = self.ai.ask(prompt)

            elapsed = perf_counter() - started

            provider = getattr(
                self.ai.provider,
                "name",
                self.ai.provider.__class__.__name__,
            )

            model = getattr(
                self.ai.provider,
                "model",
                "",
            )

            document = result["answer"]

            citations = self.citation_extractor.extract(
                document,
            )

            citations = citation_validator.validate(
                citations,
            )

            document = citation_inserter.insert(
                document,
                citations,
            )

            response = DraftResponse(
                template=template,
                document=document,
                provider=provider,
                model=model,
                processing_time=elapsed,
                word_count=len(document.split()),
                generated_at=datetime.now(UTC),
            )

            logger.info(f"Draft completed in {elapsed:.3f}s")

            return response

        except Exception:
            logger.exception("Draft generation failed.")
            raise
