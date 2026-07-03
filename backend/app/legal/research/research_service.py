from uuid import uuid4
from datetime import datetime

from app.ai.services.ai_service import AIService
from app.legal.entities.entity_extractor import LegalEntityExtractor
from app.legal.history.history import ResearchHistory
from app.legal.ranking.ranker import LegalRanker
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
            created_at=datetime.utcnow(),
        )

    def research(self, question: str):

        self.session.add_query(question)

        entities = self.entities.extract(question)

        contexts = self.search.search(question)

        ranked = self.ranker.rank(
            question,
            contexts,
        )

        answer = self.ai.ask(question)

        result = {
            "session_id": self.session.id,
            "question": question,
            "entities": entities,
            "contexts_found": len(ranked),
            "answer": answer,
        }

        self.history.add(
            question,
            result,
        )

        return result

    def get_history(self):
        return self.history.all()

    def clear_history(self):
        self.history.clear()
