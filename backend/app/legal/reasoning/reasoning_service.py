from datetime import UTC, datetime
from time import perf_counter

from app.ai.services.ai_service import AIService
from app.legal.explainability.explainer import ExplainabilityEngine
from app.legal.precedents.precedent_extractor import PrecedentExtractor
from app.legal.reasoning.schemas.reasoning_response import (
    ReasoningResponse,
)
from app.legal.reasoning.summarizer import JudgmentSummarizer


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

        started = perf_counter()

        summary = self.summarizer.summarize(text)

        precedent_data = self.precedents.extract(text)

        ai_result = self.ai.ask(summary)

        explained = self.explainer.explain(
            ai_result,
            precedent_data["precedents"],
        )

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

        return ReasoningResponse(
            answer=answer,
            reasoning=explained["reasoning"],
            citations=explained["citations"],
            provider=provider,
            model=model,
            processing_time=elapsed,
            generated_at=datetime.now(UTC),
        )
