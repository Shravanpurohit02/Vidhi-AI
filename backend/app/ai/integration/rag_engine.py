from __future__ import annotations

from app.ai.search import HybridSearch
from app.ai.citations.citation_engine import CitationEngine
from app.ai.memory.conversation import ConversationMemory


class RAGEngine:

    def __init__(self):
        self.search = HybridSearch()
        self.memory = ConversationMemory()

    def retrieve(self, query: str):
        return self.search.search(query)

    def citations(self, results):
        return CitationEngine.build(results)


    def search(
        self,
        query: str,
        provider: str | None = None,
    ):
        results = self.retrieve(query)

        return {
            "results": results,
            "citations": self.citations(results),
            "history": self.memory.history(),
        }

    def context(self, query: str):
        results = self.retrieve(query)
        return {
            "results": results,
            "citations": self.citations(results),
            "history": self.memory.history(),
        }
