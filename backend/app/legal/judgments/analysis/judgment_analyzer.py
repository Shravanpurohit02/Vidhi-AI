from __future__ import annotations

from app.legal.judgments.analysis.outcome_classifier import OutcomeClassifier
from app.legal.judgments.analysis.court_extractor import CourtExtractor


class JudgmentAnalyzer:

    def __init__(self):

        self.outcomes=OutcomeClassifier()
        self.courts=CourtExtractor()

    def analyze(self,text:str):

        return {
            "court":self.courts.extract(text),
            "outcome":self.outcomes.classify(text),
        }
