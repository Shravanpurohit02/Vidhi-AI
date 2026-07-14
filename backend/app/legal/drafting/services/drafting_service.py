from __future__ import annotations

from app.ai.integration.chat_service import ChatService
from app.legal.drafting.services.citation_service import DraftCitationService
from app.legal.drafting.services.prompt_service import PromptService


class DraftingService:

    def __init__(self):
        self.prompt = PromptService()
        self.chat = AIService()
        self.citations = DraftCitationService()

    def generate(
        self,
        conversation_id: str,
        template: str,
        facts: str,
        provider: str | None = None,
    ) -> str:

        prompt = self.prompt.build(
            template=template,
            facts=facts,
        )

        response = self.chat.chat(
            conversation_id=conversation_id,
            message=prompt,
            provider=provider,
        )

        return self.citations.append(
            response["response"],
            response["citations"],
        )
