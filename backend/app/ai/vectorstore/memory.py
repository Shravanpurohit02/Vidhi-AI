from __future__ import annotations

import math


class MemoryVectorStore:

    def __init__(self):
        self.items: list[dict] = []

    def add(
        self,
        embedding,
        metadata,
        text,
    ):
        self.items.append(
            {
                "id": len(self.items) + 1,
                "embedding": embedding,
                "metadata": metadata,
                "text": text,
            }
        )

    def all(self):
        return list(self.items)

    def count(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def delete(
        self,
        vector_id,
    ):
        self.items = [item for item in self.items if item["id"] != vector_id]

    @staticmethod
    def _cosine(a, b):

        dot = sum(x * y for x, y in zip(a, b))

        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(y * y for y in b))

        if na == 0 or nb == 0:
            return 0.0

        return dot / (na * nb)

    def search(
        self,
        embedding,
        top_k=5,
    ):

        scored = []

        for item in self.items:

            result = dict(item)

            result["score"] = self._cosine(
                embedding,
                item["embedding"],
            )

            scored.append(result)

        scored.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return scored[:top_k]
