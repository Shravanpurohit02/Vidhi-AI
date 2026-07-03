class BM25Search:

    def search(
        self,
        query: str,
        documents,
    ):
        query_words = {
            word.lower()
            for word in query.split()
        }

        scored = []

        for doc in documents:

            text = doc[0]

            score = sum(
                word.lower() in text.lower()
                for word in query_words
            )

            scored.append(
                (
                    score,
                    doc,
                )
            )

        scored.sort(
            reverse=True,
            key=lambda x: x[0],
        )

        return [
            item[1]
            for item in scored
        ]
