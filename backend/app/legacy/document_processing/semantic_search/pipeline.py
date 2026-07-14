from __future__ import annotations

from app.document_processing.semantic_search.metadata_filter import MetadataFilter
from app.document_processing.semantic_search.rrf import ReciprocalRankFusion
from app.document_processing.semantic_search.score_normalizer import ScoreNormalizer
from app.document_processing.semantic_search.confidence import ConfidenceScorer
from app.ai.search.hybrid_search import HybridSearchService


class SemanticSearchPipeline:

    def __init__(self):

        self.search=HybridSearchService()
        self.rrf=ReciprocalRankFusion()

    def query(self,query,top_k=10,filters=None):

        results=self.search.search(query,top_k)

        results=ScoreNormalizer.normalize(results)

        results=MetadataFilter.apply(results,filters)

        for item in results:
            item.metadata["confidence"]=ConfidenceScorer.label(item.score)

        return results


# Backward compatibility
HybridSearchPipeline = SemanticSearchPipeline
