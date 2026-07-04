from collections import defaultdict
from typing import Callable, Any


class EventBus:

    def __init__(self):
        self._handlers = defaultdict(list)

    def subscribe(
        self,
        event: str,
        handler: Callable[[dict], Any],
    ):
        self._handlers[event].append(handler)

    async def publish(
        self,
        event: str,
        payload: dict,
    ):
        results = []

        for handler in self._handlers[event]:
            results.append(
                await handler(payload)
            )

        return results
