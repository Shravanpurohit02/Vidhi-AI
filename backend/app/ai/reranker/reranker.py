class Reranker:

    def rerank(
        self,
        query,
        results,
    ):

        return sorted(
            results,
            key=lambda r: len(r[0]),
            reverse=True,
        )
