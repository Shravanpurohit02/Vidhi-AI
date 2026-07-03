from app.ai.services.ai_service import AIService
from app.legal.parsers.legal_parser import LegalParser


class KnowledgeBase:

    def __init__(self):

        self.ai = AIService()
        self.parser = LegalParser()

    def ingest_file(
        self,
        path: str,
        metadata: dict,
    ):

        parsed = self.parser.parse(path)

        self.ai.ingest_document(
            parsed["text"],
            metadata,
        )

        return parsed
