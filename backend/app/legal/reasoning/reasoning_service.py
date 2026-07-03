from app.ai.services.ai_service import AIService
from app.legal.explainability.explainer import ExplainabilityEngine
from app.legal.precedents.precedent_extractor import PrecedentExtractor
from app.legal.reasoning.summarizer import JudgmentSummarizer


class ReasoningService:

    def __init__(self):

        self.ai = AIService()
        self.summarizer = JudgmentSummarizer()
        self.precedents = PrecedentExtractor()
        self.explainer = ExplainabilityEngine()

    def analyze(
        self,
        text: str,
    ):

        summary = self.summarizer.summarize(text)

        precedent_data = self.precedents.extract(text)

        ai_response = self.ai.ask(summary)

        return self.explainer.explain(
            ai_response,
            precedent_data["precedents"],
        )
