from __future__ import annotations

from app.ai.bm25.document_loader import DocumentLoader
from app.ai.bm25.index import BM25Index


class BM25Engine:

    def __init__(self):
        self.index=BM25Index()

    def rebuild(self):

        self.index.build(
            DocumentLoader.load()
        )

    def search(
        self,
        query:str,
        top_k:int=10,
    ):

        self.rebuild()

        return self.index.search(
            query=query,
            top_k=top_k,
        )
