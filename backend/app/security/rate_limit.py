from __future__ import annotations

from collections import defaultdict, deque
from threading import Lock
from time import time


class RateLimiter:
    def __init__(self):
        self._requests = defaultdict(deque)
        self._lock = Lock()

    def allow(
        self,
        key: str,
        limit: int,
        window_seconds: int,
    ) -> bool:
        now = time()

        with self._lock:
            bucket = self._requests[key]

            while bucket and bucket[0] <= now - window_seconds:
                bucket.popleft()

            if len(bucket) >= limit:
                return False

            bucket.append(now)
            return True


limiter = RateLimiter()
