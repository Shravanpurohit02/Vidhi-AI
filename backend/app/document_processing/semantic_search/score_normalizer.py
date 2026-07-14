from __future__ import annotations

class ScoreNormalizer:

    @staticmethod
    def normalize(results):
        if not results:
            return results

        scores=[r.score for r in results]
        lo=min(scores)
        hi=max(scores)

        if hi==lo:
            return results

        for r in results:
            r.score=(r.score-lo)/(hi-lo)

        return results
