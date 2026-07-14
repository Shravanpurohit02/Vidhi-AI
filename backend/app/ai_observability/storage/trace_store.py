from collections import deque

from app.ai_observability.models.trace import AITrace


class TraceStore:
    def __init__(self, limit: int = 1000):
        self._traces = deque(maxlen=limit)

    def add(self, trace: AITrace):
        self._traces.append(trace)

    def all(self):
        return list(self._traces)

    def clear(self):
        self._traces.clear()


trace_store = TraceStore()
