class LegalRanker:

    def rank(self, query: str, contexts: list):

        ranked = sorted(
            contexts,
            key=lambda item: (
                len(item.get("text", "")),
                item.get("metadata", {}).get("source", ""),
            ),
            reverse=True,
        )

        return ranked
