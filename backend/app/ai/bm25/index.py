from __future__ import annotations

import math
from collections import Counter


class BM25Index:

    def __init__(self):
        self.documents = []
        self.doc_freq = Counter()
        self.avgdl = 0.0

    def build(self, documents: list[tuple[int, str]]):

        self.documents.clear()
        self.doc_freq.clear()

        total_len = 0

        for doc_id, text in documents:

            tokens = text.lower().split()

            self.documents.append(
                {
                    "id": doc_id,
                    "tokens": tokens,
                    "tf": Counter(tokens),
                }
            )

            total_len += len(tokens)

            for token in set(tokens):
                self.doc_freq[token] += 1

        self.avgdl = (
            total_len / len(self.documents)
            if self.documents else 0
        )

    def search(
        self,
        query: str,
        top_k: int = 10,
    ):

        q = query.lower().split()

        N = len(self.documents)

        scores = []

        for doc in self.documents:

            score = 0.0
            dl = len(doc["tokens"])

            for term in q:

                tf = doc["tf"].get(term, 0)

                if tf == 0:
                    continue

                df = self.doc_freq.get(term, 1)

                idf = math.log((N - df + 0.5) / (df + 0.5) + 1)

                k1 = 1.5
                b = 0.75

                score += idf * (
                    tf * (k1 + 1)
                ) / (
                    tf + k1 * (1 - b + b * dl / max(self.avgdl, 1))
                )

            scores.append(
                {
                    "document_id": doc["id"],
                    "score": score,
                }
            )

        scores.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scores[:top_k]
