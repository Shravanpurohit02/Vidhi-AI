from app.legal.reasoning.strategies.general import (
    GeneralAnalysisStrategy,
)
from app.legal.reasoning.strategies.irac import (
    IRACStrategy,
)
from app.legal.reasoning.strategies.judgment import (
    JudgmentAnalysisStrategy,
)
from app.legal.reasoning.strategies.statutory import (
    StatutoryInterpretationStrategy,
)


class ReasoningStrategyRegistry:

    def __init__(self):

        self._strategies = {
            "general_analysis": GeneralAnalysisStrategy(),
            "irac": IRACStrategy(),
            "judgment_analysis": JudgmentAnalysisStrategy(),
            "statutory_interpretation": (StatutoryInterpretationStrategy()),
        }

    def get(
        self,
        name: str = "general_analysis",
    ):

        return self._strategies.get(
            name,
            self._strategies["general_analysis"],
        )


registry = ReasoningStrategyRegistry()
