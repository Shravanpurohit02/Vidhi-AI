from datetime import UTC, datetime
from time import perf_counter
from uuid import uuid4

from app.ai.services.ai_service import AIService
from app.core.logging import get_logger
from app.legal.entities.entity_extractor import LegalEntityExtractor
from app.legal.history.history import ResearchHistory
from app.legal.ranking.ranker import LegalRanker
from app.legal.research.confidence import ConfidenceEngine
from app.legal.research.schemas.research_response import (
    ResearchResponse,
)
from app.legal.search.semantic_search import SemanticSearch
from app.legal.session.session import ResearchSession

logger = get_logger()


class LegalResearchService:

    def __init__(self):
        self.ai = AIService()
        self.entities = LegalEntityExtractor()
        self.search = SemanticSearch()
        self.ranker = LegalRanker()
        self.confidence = ConfidenceEngine()
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

    def research(
        self,
        question: str,
    ) -> ResearchResponse:

        logger.info(f"Research started: {question}")

        started = perf_counter()

        try:

            self.session.add_query(question)

            entities = self.entities.extract(question)

            logger.info(f"Extracted {len(entities)} entity groups.")

            contexts = self.search.search(question)

            logger.info(f"Retrieved {len(contexts)} contexts.")

            ranked = self.ranker.rank(
                question,
                contexts,
            )

            logger.info(f"Ranked {len(ranked)} contexts.")

            ai_result = self.ai.ask(question)

            logger.info("AI answer generated.")

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

            citations = ai_result.get(
                "citations",
                [],
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
                confidence=self.confidence.calculate(
                    retrieval_score=1.0 if contexts else 0.0,
                    rerank_score=1.0 if ranked else 0.0,
                    citation_count=len(citations),
                    context_count=len(ranked),
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

            logger.info(
                f"Research completed in {elapsed:.3f}s "
                f"(confidence={response.confidence:.3f})"
            )

            return response

        except Exception:

            logger.exception("Legal research failed.")

            raise

    def get_history(self):
        return self.history.all()

    def clear_history(self):
        self.history.clear()
