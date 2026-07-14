from app.legal.reasoning.strategies import registry


class ExplainabilityEngine:
    """
    Produces explainability metadata for legal reasoning.
    """

    def _confidence(
        self,
        answer: str,
        citations: list,
    ) -> float:

        score = 0.50

        if answer:
            score += 0.15

        score += min(len(citations), 5) * 0.05

        return min(score, 1.0)

    def _explainability(
        self,
        answer: str,
        reasoning: str,
        citations: list,
    ) -> float:

        score = 0.0

        if reasoning:
            score += 0.60

        if answer:
            score += 0.20

        if citations:
            score += 0.20

        return min(score, 1.0)

    def explain(
        self,
        answer,
        citations,
        strategy: str = "general_analysis",
    ):

        if isinstance(answer, dict):
            answer_text = answer.get("answer", "")
        else:
            answer_text = str(answer)

        reasoning_strategy = registry.get(strategy)

        reasoning = reasoning_strategy.build_reasoning(
            answer_text,
            citations,
        )

        return {
            "answer": answer,
            "reasoning": reasoning,
            "reasoning_strategy": reasoning_strategy.name,
            "confidence": self._confidence(
                answer_text,
                citations,
            ),
            "explainability_score": self._explainability(
                answer_text,
                reasoning,
                citations,
            ),
            "citation_support": len(citations),
            "citations": citations,
        }
