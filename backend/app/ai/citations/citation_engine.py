class CitationEngine:

    @staticmethod
    def build(contexts):

        citations = []

        for item in contexts:

            metadata = item.get("metadata", {})

            citations.append(
                {
                    "source": metadata.get("source", "Unknown"),
                    "reference": metadata,
                }
            )

        return citations
