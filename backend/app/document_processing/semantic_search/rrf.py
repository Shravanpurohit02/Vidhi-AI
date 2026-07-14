from __future__ import annotations


class ReciprocalRankFusion:

    def fuse(
        self,
        lexical: list,
        semantic: list,
        k: int = 60,
    ) -> list:

        scores = {}

        for rank, item in enumerate(lexical, start=1):
            key = getattr(item, "chunk_id", id(item))
            scores.setdefault(key, {"item": item, "score": 0.0})
            scores[key]["score"] += 1.0 / (k + rank)

        for rank, item in enumerate(semantic, start=1):
            key = getattr(item, "chunk_id", id(item))
            scores.setdefault(key, {"item": item, "score": 0.0})
            scores[key]["score"] += 1.0 / (k + rank)

        return [
            value["item"]
            for value in sorted(
                scores.values(),
                key=lambda x: x["score"],
                reverse=True,
            )
        ]
