from __future__ import annotations

class CitationGraph:

    def __init__(self):
        self.graph={}

    def add(
        self,
        source:str,
        target:str,
    ):
        self.graph.setdefault(source,set()).add(target)

    def neighbours(
        self,
        citation:str,
    ):
        return sorted(self.graph.get(citation,set()))
