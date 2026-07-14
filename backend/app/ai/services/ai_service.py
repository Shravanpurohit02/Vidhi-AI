from __future__ import annotations

from app.ai.search.hybrid_search import HybridSearch
from app.ai.config import DEFAULT_PROVIDER
from app.ai.citations.citation_engine import CitationEngine
from app.ai.memory.conversation import ConversationMemory
from app.ai.prompts.system import LEGAL_SYSTEM_PROMPT
from app.ai.retrieval.search import Retriever



from app.ai.providers.base.bootstrap import ProviderBootstrap
from app.ai.providers.base.router import CapabilityRouter
from app.ai.providers.capabilities import Capability

class AIService:

    def __init__(self):

        self.search = HybridSearch()
        self.memory = ConversationMemory()

        self.provider_registry = ProviderBootstrap().build()
        self.router = CapabilityRouter(
            self.provider_registry,
        )
        self.default_provider = DEFAULT_PROVIDER

    def set_provider(
        self,
        provider_name: str,
    ) -> None:
        self.default_provider = provider_name

    def available_capabilities(self) -> dict[str, bool]:
        provider = self.router.registry.get(
            self.default_provider or DEFAULT_PROVIDER
        )
        return provider.capabilities

    def ingest_document(
        self,
        text: str,
        metadata: dict,
        document_id: int | None = None,
    ) -> None:
        self.search.index_document(
            document_id=document_id,
            text=text,
            metadata=metadata,
        )

    def ask(
        self,
        question: str,
        **kwargs,
    ):

        self.memory.add("user", question)

        contexts = self.search.search(question)

        context_parts = []

        for item in contexts:

            if hasattr(item, "text"):
                context_parts.append(item.text)

            elif hasattr(item, "metadata"):
                metadata = item.metadata or {}
                context_parts.append(
                    metadata.get("text", "")
                )

            elif isinstance(item, dict):
                context_parts.append(item.get("text", ""))

        context_text = "\n\n".join(
            part for part in context_parts if part
        )

        citations = CitationEngine.build(contexts)

        prompt = f"""
Conversation:
{self.memory.history()}

Context:
{context_text}

Question:
{question}

Answer ONLY from the supplied legal context.
If insufficient information exists,
clearly state that.
"""

        answer = self.router.chat(
            prompt=prompt,
            system_prompt=LEGAL_SYSTEM_PROMPT,
            preferred_provider=getattr(self, "default_provider", DEFAULT_PROVIDER),
            **kwargs,
        )

        self.memory.add(
            "assistant",
            answer,
        )

        return {
            "provider": getattr(self, "default_provider", DEFAULT_PROVIDER),
            "model": "auto",
            "answer": answer,
            "citations": citations,
            "capabilities": self.available_capabilities(),
        }