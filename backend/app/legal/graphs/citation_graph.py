class CitationGraph:

    def __init__(self):
        self.graph = {}

    def add_document(
        self,
        document: str,
        citations: list[str],
    ):

        self.graph[document] = citations

    def neighbours(
        self,
        document: str,
    ):
        return self.graph.get(document, [])
