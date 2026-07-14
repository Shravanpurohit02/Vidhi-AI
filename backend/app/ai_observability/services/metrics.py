from app.ai_observability.storage.trace_store import trace_store


class AIMetrics:

    def summary(self):
        traces = trace_store.all()

        total = len(traces)

        if total == 0:
            return {
                "requests": 0,
                "avg_latency_ms": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "estimated_cost": 0,
            }

        return {
            "requests": total,
            "avg_latency_ms": round(
                sum(t.latency_ms for t in traces) / total,
                2,
            ),
            "input_tokens": sum(
                t.input_tokens for t in traces
            ),
            "output_tokens": sum(
                t.output_tokens for t in traces
            ),
            "estimated_cost": round(
                sum(t.estimated_cost for t in traces),
                6,
            ),
        }


ai_metrics = AIMetrics()
