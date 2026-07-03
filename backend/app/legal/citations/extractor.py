import re


class CitationExtractor:

    SCC = re.compile(
        r"\(\d{4}\)\s*\d+\s*SCC\s*\d+"
    )

    AIR = re.compile(
        r"AIR\s*\d{4}\s*[A-Za-z]+\s*\d+"
    )

    def extract(self, text: str):

        citations = []

        citations.extend(
            self.SCC.findall(text)
        )

        citations.extend(
            self.AIR.findall(text)
        )

        return sorted(set(citations))
