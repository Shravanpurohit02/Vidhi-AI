from __future__ import annotations

class CrossEncoder:

    def rerank(
        self,
        query:str,
        results:list,
    ):

        for item in results:
            score=getattr(item,"score",0.0)
            item.score=min(score*1.05,1.0)

        results.sort(
            key=lambda x:x.score,
            reverse=True,
        )

        return results
