from datetime import UTC, datetime
from time import perf_counter
from uuid import uuid4

from app.ai.services.ai_service import AIService
from app.legal.entities.entity_extractor import LegalEntityExtractor
from app.legal.history.history import ResearchHistory
from app.legal.ranking.ranker import LegalRanker
from app.legal.research.schemas.research_response import (
    Citation,
    ResearchResponse,
)
from app.legal.search.semantic_search import SemanticSearch
from app.legal.session.session import ResearchSession


class LegalResearchService:

    def __init__(self):
        self.ai = AIService()
        self.entities = LegalEntityExtractor()
        self.search = SemanticSearch()
        self.ranker = LegalRanker()
        self.history = ResearchHistory()

        self.session = ResearchSession(
            id=str(uuid4()),
            created_at=datetime.now(UTC),
        )

    def _summary(self, answer: str) -> str:
        answer = answer.strip()
        if len(answer) <= 300:
            return answer
        return answer[:297] + "..."

    def _confidence(self, contexts_found: int) -> float:
        if contexts_found <= 0:
            return 0.0
        return min(1.0, contexts_found / 10)

    def research(
        self,
        question: str,
    ) -> ResearchResponse:

        started = perf_counter()

        self.session.add_query(question)

        entities = self.entities.extract(question)

        contexts = self.search.search(question)

        ranked = self.ranker.rank(
            question,
            contexts,
        )

        ai_result = self.ai.ask(question)

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

        citations = []

        for item in ai_result.get("citations", []):
            citations.append(
                Citation(
                    title=str(item),
                    source="retriever",
                )
            )

        response = ResearchResponse(
            session_id=self.session.id,
            question=question,
            answer=ai_result["answer"],
            summary=self._summary(
                ai_result["answer"],
            ),
            entities=entities,
            contexts_found=len(ranked),
            citations=citations,
            sources=["retriever"] if ranked else [],
            confidence=self._confidence(
                len(ranked),
            ),
            provider=provider,
            model=model,
            processing_time=elapsed,
            created_at=datetime.now(UTC),
        )

        self.history.add(
            question,
            response.model_dump(),
        )

        return response

    def get_history(self):
        return self.history.all()

    def clear_history(self):
        self.history.clear()
