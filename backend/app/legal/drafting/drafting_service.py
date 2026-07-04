from datetime import UTC, datetime
from time import perf_counter

from app.ai.services.ai_service import AIService
from app.legal.drafting.schemas.draft_response import (
    DraftResponse,
)
from app.legal.templates.templates import TEMPLATES


class DraftingService:

    def __init__(self):
        self.ai = AIService()

    def generate(
        self,
        template: str,
        facts: str,
        relief: str = "",
    ) -> DraftResponse:

        if template not in TEMPLATES:
            raise ValueError("Unknown template")

        prompt = TEMPLATES[template].format(
            facts=facts,
            relief=relief,
        )

        started = perf_counter()

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

        return DraftResponse(
            template=template,
            document=document,
            provider=provider,
            model=model,
            processing_time=elapsed,
            word_count=len(document.split()),
            generated_at=datetime.now(UTC),
        )
