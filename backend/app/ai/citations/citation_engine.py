from app.legal.research.schemas.research_response import Citation


class CitationEngine:

    @staticmethod
    def build(contexts) -> list[Citation]:

        citations: list[Citation] = []

        for item in contexts:

            if hasattr(item, "metadata"):
                metadata = item.metadata or {}

                if hasattr(item, "score"):
                    metadata.setdefault("score", item.score)

                if hasattr(item, "document_id"):
                    metadata.setdefault("document_id", item.document_id)

                if hasattr(item, "chunk_id"):
                    metadata.setdefault("chunk_id", item.chunk_id)

            elif isinstance(item, dict):
                metadata = item.get("metadata", {})

            else:
                metadata = {}

            citations.append(
                Citation(
                    title=metadata.get(
                        "title",
                        metadata.get(
                            "filename",
                            metadata.get(
                                "source",
                                "Unknown",
                            ),
                        ),
                    ),
                    citation=metadata.get(
                        "citation",
                        "",
                    ),
                    court=metadata.get(
                        "court",
                        "",
                    ),
                    year=metadata.get(
                        "year",
                    ),
                    judge=metadata.get(
                        "judge",
                        "",
                    ),
                    bench=metadata.get(
                        "bench",
                        "",
                    ),
                    paragraphs=metadata.get(
                        "paragraphs",
                        [],
                    ),
                    document_id=str(
                        metadata.get(
                            "document_id",
                            "",
                        )
                    ),
                    source=metadata.get(
                        "source",
                        "Unknown",
                    ),
                    url=metadata.get(
                        "url",
                        "",
                    ),
                    score=float(
                        metadata.get(
                            "score",
                            0.0,
                        )
                    ),
                )
            )

        return citations
