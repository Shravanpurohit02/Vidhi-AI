import time
from datetime import datetime, UTC

from app.legal.research.pipeline.research_pipeline import (
    ResearchPipeline,
)
from app.legal.research.schemas.research_response import (
    ResearchResponse,
)


class ResearchOrchestrator:

    def __init__(self):
        self.pipeline = ResearchPipeline()

    def research(
        self,
        question: str,
    ) -> ResearchResponse:

        start = time.perf_counter()

        result = self.pipeline.execute(question)

        elapsed = time.perf_counter() - start

        return ResearchResponse(
            session_id="",
            question=question,
            answer=result["answer"],
            summary=result["answer"][:300],
            confidence=1.0 if result["citations"] else 0.5,
            citations=result.get("citations", []),
            sources=result.get("sources", []),
            provider=result.get("provider", ""),
            model=result.get("model", ""),
            processing_time=elapsed,
            created_at=datetime.now(UTC),
        )
