from __future__ import annotations

from app.legal.citations.extractor import CitationExtractor
from app.legal.citations.matcher import CitationMatcher
from app.legal.citations.graph import CitationGraph


class CitationService:

    def __init__(self):
        self.extractor=CitationExtractor()
        self.matcher=CitationMatcher()
        self.graph=CitationGraph()

    def analyse(
        self,
        text:str,
    ):

        citations=self.extractor.extract(text)

        citations=self.matcher.match(citations)

        return citations
