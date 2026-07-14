from app.legal.reasoning.strategies.base import BaseReasoningStrategy


class GeneralAnalysisStrategy(BaseReasoningStrategy):

    name = "general_analysis"

    def build_reasoning(
        self,
        answer: str,
        citations: list,
    ) -> str:

        return (
            "The conclusion was generated using retrieved legal "
            "materials, supporting precedents, and available citations."
        )
