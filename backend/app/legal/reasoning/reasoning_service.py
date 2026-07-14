from datetime import UTC, datetime
from time import perf_counter

from app.ai.services.ai_service import AIService
from app.core.logging import get_logger
from app.legal.explainability.explainer import ExplainabilityEngine
from app.legal.precedents.precedent_extractor import PrecedentExtractor
from app.legal.reasoning.schemas.reasoning_response import (
    ReasoningResponse,
)
from app.legal.reasoning.summarizer import JudgmentSummarizer

logger = get_logger()


class ReasoningService:

    def __init__(self):

        self.ai = AIService()
        self.summarizer = JudgmentSummarizer()
        self.precedents = PrecedentExtractor()
        self.explainer = ExplainabilityEngine()

    def analyze(
        self,
        text: str,
    ) -> ReasoningResponse:

        logger.info("Reasoning analysis started.")

        started = perf_counter()

        try:

            summary = self.summarizer.summarize(text)

            logger.info("Judgment summarized.")

            precedent_data = self.precedents.extract(text)

            logger.info(f"Extracted {len(precedent_data['precedents'])} precedents.")

            ai_result = self.ai.ask(summary)

            logger.info("AI reasoning generated.")

            explained = self.explainer.explain(
                ai_result,
                precedent_data["precedents"],
            )

            logger.info("Explainability completed.")

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

            answer = explained["answer"]

            if isinstance(answer, dict):
                answer = answer.get("answer", "")

            response = ReasoningResponse(
                answer=answer,
                reasoning=explained["reasoning"],
                citations=explained["citations"],
                confidence=explained["confidence"],
                reasoning_strategy=explained["reasoning_strategy"],
                explainability_score=explained["explainability_score"],
                citation_support=explained["citation_support"],
                provider=provider,
                model=model,
                processing_time=elapsed,
                generated_at=datetime.now(UTC),
            )

            logger.info(f"Reasoning completed in {elapsed:.3f}s.")

            return response

        except Exception:

            logger.exception("Reasoning analysis failed.")

            raise
