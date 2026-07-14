from __future__ import annotations

from app.ai.integration.citation_manager import CitationManager
from app.ai.integration.context_builder import ContextBuilder
from app.ai.integration.conversation_manager import ConversationManager
from app.ai.integration.hallucination_guard import HallucinationGuard
from app.ai.integration.prompt_builder import PromptBuilder
from app.ai.integration.provider_router import ProviderRouter
from app.ai.integration.rag_engine import RAGEngine
from app.ai.integration.response_validator import ResponseValidator


class ChatService:

    def __init__(self):
        self.prompt = PromptBuilder()
        self.context = ContextBuilder()
        self.router = ProviderRouter()
        self.rag = RAGEngine()
        self.validator = ResponseValidator()
        self.guard = HallucinationGuard()
        self.citations = CitationManager()
        self.memory = ConversationManager()

    def chat(
        self,
        conversation_id: str,
        message: str,
        provider: str | None = None,
    ) -> dict:

        self.memory.add_user(
            conversation_id,
            message,
        )

        rag = self.rag.search(
            query=message,
            provider=provider,
        )

        context = self.context.build([item.text for item in rag["results"]])

        prompt = self.prompt.build(
            system_prompt="You are Vidhi AI.",
            context=context,
            user_prompt=message,
        )

        model = self.router.select(provider)

        response = model.generate(prompt)

        if not self.validator.validate(response):
            raise RuntimeError("Invalid AI response.")

        checked = self.guard.review(
            response,
            rag["citations"],
        )

        self.memory.add_assistant(
            conversation_id,
            checked["response"],
        )

        return {
            "response": checked["response"],
            "citations": self.citations.format(rag["citations"]),
        }
