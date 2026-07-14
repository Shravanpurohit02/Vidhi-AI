from __future__ import annotations

from app.legal.drafting.services.drafting_service import DraftingService


class DocumentGenerator:

    def __init__(self):
        self.service = DraftingService()

    def generate(
        self,
        conversation_id: str,
        template: str,
        facts: str,
        provider: str | None = None,
    ) -> str:

        return self.service.generate(
            conversation_id,
            template,
            facts,
            provider,
        )
