import re


class LegalEntityExtractor:

    ARTICLES = re.compile(r"Article\s+\d+[A-Za-z]*", re.IGNORECASE)
    SECTIONS = re.compile(r"Section\s+\d+[A-Za-z]*", re.IGNORECASE)
    ACTS = re.compile(r"[A-Z][A-Za-z ]+ Act(?:,? \d{4})?")

    def extract(self, text: str):

        return {
            "articles": sorted(set(self.ARTICLES.findall(text))),
            "sections": sorted(set(self.SECTIONS.findall(text))),
            "acts": sorted(set(self.ACTS.findall(text))),
        }
