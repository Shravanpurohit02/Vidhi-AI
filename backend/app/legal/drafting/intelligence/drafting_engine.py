from __future__ import annotations

from app.legal.drafting.intelligence.template_selector import TemplateSelector
from app.legal.drafting.intelligence.clause_recommender import ClauseRecommender


class DraftingEngine:

    def __init__(self):

        self.templates=TemplateSelector()
        self.clauses=ClauseRecommender()

    def analyze(self,query:str):

        template=self.templates.select(query)

        return {
            "template":template,
            "clauses":self.clauses.recommend(template),
        }
