class ExplainabilityEngine:

    def explain(
        self,
        answer,
        citations,
    ):

        return {
            "answer": answer,
            "reasoning": (
                "The answer was generated using the retrieved legal context "
                "and supporting citations."
            ),
            "citations": citations,
        }
