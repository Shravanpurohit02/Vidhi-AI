from app.ai.services.ai_service import AIService


class ResearchPipeline:

    def __init__(self):
        self.ai = AIService()

    def execute(
        self,
        question: str,
    ) -> dict:

        result = self.ai.ask(question)

        result["provider"] = getattr(
            self.ai.provider,
            "name",
            "",
        )

        result["model"] = getattr(
            self.ai.provider,
            "model",
            "",
        )

        return result
