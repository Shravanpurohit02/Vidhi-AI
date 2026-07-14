from __future__ import annotations

import time
import uuid
from contextlib import contextmanager

from app.ai_observability.models.trace import AITrace
from app.ai_observability.storage.trace_store import trace_store


class AITracingService:

    @contextmanager
    def trace(
        self,
        *,
        feature: str,
        provider: str,
        model: str,
        prompt: str = "",
    ):
        trace = AITrace(
            trace_id=str(uuid.uuid4()),
            feature=feature,
            provider=provider,
            model=model,
            prompt=prompt,
        )

        start = time.perf_counter()

        try:
            yield trace
        finally:
            trace.latency_ms = (
                time.perf_counter() - start
            ) * 1000

            trace_store.add(trace)


ai_tracing = AITracingService()
