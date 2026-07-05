class Reranker:

    def rerank(
        self,
        query,
        results,
    ):

        query_words = {word.lower() for word in query.split()}

        def score(item):
            text = item.get("text", "").lower()

            return sum(word in text for word in query_words)

        return sorted(
            results,
            key=score,
            reverse=True,
        )
