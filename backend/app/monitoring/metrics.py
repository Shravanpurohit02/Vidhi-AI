from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

METRICS_FILE = Path("logs/metrics.json")
METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)


class Metrics:

    def __init__(self):
        self.counter: dict[str, int] = Counter()

    def increment(
        self,
        name: str,
    ):
        self.counter[name] += 1

        METRICS_FILE.write_text(
            json.dumps(
                dict(self.counter),
                indent=2,
            ),
            encoding="utf-8",
        )

    def snapshot(self):
        return dict(self.counter)


metrics = Metrics()
