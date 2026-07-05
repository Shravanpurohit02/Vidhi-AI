from app.ai.config import DEFAULT_PROVIDER
from app.ai.citations.citation_engine import CitationEngine
from app.ai.memory.conversation import ConversationMemory
from app.ai.prompts.system import LEGAL_SYSTEM_PROMPT
from app.ai.providers.mock_provider import MockAIProvider
from app.ai.providers.registry import registry
from app.ai.providers.loader import load_providers
from app.ai.providers.provider_selector import selector
from app.ai.retrieval.retriever import Retriever


class AIService:

    def __init__(self):
        load_providers()

        if "mock" not in registry.providers():
            registry.register(
                "mock",
                MockAIProvider(),
            )

        try:
            self.provider = registry.get(DEFAULT_PROVIDER)
        except Exception:
            self.provider = selector.select()
        self.retriever = Retriever()
        self.memory = ConversationMemory()

    def ingest_document(self, text: str, metadata: dict):
        self.retriever.index_document(text, metadata)

    def ask(self, question: str):

        self.memory.add("user", question)

        contexts = self.retriever.retrieve(question)

        context_text = "\n\n".join(item["text"] for item in contexts)

        citations = CitationEngine.build(contexts)

        prompt = f"""
Conversation:
{self.memory.history()}

Context:
{context_text}

Question:
{question}

Answer only from the supplied legal context.
If insufficient information exists, clearly state that.
"""

        answer = self.provider.generate(
            prompt=prompt,
            system_prompt=LEGAL_SYSTEM_PROMPT,
        )

        self.memory.add("assistant", answer)

        return {
            "answer": answer,
            "citations": citations,
        }
