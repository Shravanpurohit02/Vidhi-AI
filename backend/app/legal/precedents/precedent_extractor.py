from app.legal.citations.extractor import CitationExtractor


class PrecedentExtractor:

    def __init__(self):
        self.extractor = CitationExtractor()

    def extract(self, text: str):

        return {
            "precedents": self.extractor.extract(text)
        }
