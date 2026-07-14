from __future__ import annotations

from app.legal.reasoning.analysis.issue_identifier import IssueIdentifier
from app.legal.reasoning.analysis.statute_mapper import StatuteMapper


class LegalReasoningEngine:

    def __init__(self):

        self.issues=IssueIdentifier()
        self.mapper=StatuteMapper()

    def analyze(self,text:str):

        issues=self.issues.identify(text)

        return {
            "issues":issues,
            "statutes":self.mapper.map(issues),
        }
