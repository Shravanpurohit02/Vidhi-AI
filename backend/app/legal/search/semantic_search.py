from app.ai.services.ai_service import AIService


class SemanticSearch:

    def __init__(self):
        self.ai = AIService()

    def search(self, query: str):
        return self.ai.search.search(query)
