from __future__ import annotations

from app.ai.search.pipeline import SemanticSearchPipeline
from app.ai.reranker.service import RerankerService
from app.legal.research.core.query_analyzer import QueryAnalyzer
from app.legal.research.core.intent_classifier import IntentClassifier
from app.legal.research.core.query_expander import QueryExpander
from app.legal.research.core.result_deduplicator import ResultDeduplicator
from app.legal.research.core.result_formatter import ResultFormatter
from app.legal.reasoning.analysis import LegalReasoningEngine
from app.legal.judgments.analysis import JudgmentAnalyzer
from app.legal.drafting.intelligence import DraftingEngine
from app.agents.orchestration import WorkflowEngine


class ResearchPipeline:

    def __init__(self):

        self.search=SemanticSearchPipeline()
        self.reranker=RerankerService()
        self.analyzer=QueryAnalyzer()
        self.intent=IntentClassifier()
        self.expander=QueryExpander()
        self.deduplicator=ResultDeduplicator()
        self.formatter=ResultFormatter()
        self.reasoning=LegalReasoningEngine()
        self.judgments=JudgmentAnalyzer()
        self.drafting=DraftingEngine()
        self.workflow=WorkflowEngine()

    def search(self,query:str):

        query=self.expander.expand(query)
        analysis=self.analyzer.analyze(query)

        results=self.search.query(
            analysis["normalized"]
        )

        results=self.reranker.rerank(
            analysis["normalized"],
            results,
        )

        results=self.deduplicator.deduplicate(results)

        reasoning=self.reasoning.analyze(query)
        judgment=self.judgments.analyze(query)
        drafting=self.drafting.analyze(query)
        workflow=self.workflow.route(query)

        return {
            "intent":self.intent.classify(query),
            "analysis":analysis,
            "results":self.formatter.format(results),
            "reasoning":reasoning,
            "judgment":judgment,
            "drafting":drafting,
            "workflow":workflow,
        }
