from app.legal.knowledge.knowledge_base import KnowledgeBase


class CorpusManager:

    def __init__(self):
        self.kb = KnowledgeBase()

    def ingest_directory(
        self,
        directory: str,
    ):
        return self.kb.ingest_directory(directory)

    def statistics(
        self,
        directory: str,
    ):
        return self.kb.statistics(directory)
