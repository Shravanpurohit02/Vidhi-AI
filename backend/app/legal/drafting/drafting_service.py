from app.ai.services.ai_service import AIService
from app.legal.templates.templates import TEMPLATES


class DraftingService:

    def __init__(self):
        self.ai = AIService()

    def generate(
        self,
        template: str,
        facts: str,
        relief: str = "",
    ):

        if template not in TEMPLATES:
            raise ValueError("Unknown template")

        prompt = TEMPLATES[template].format(
            facts=facts,
            relief=relief,
        )

        return self.ai.ask(prompt)
