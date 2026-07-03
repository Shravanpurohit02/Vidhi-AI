from collections import Counter


class Metrics:

    def __init__(self):
        self.counter = Counter()

    def increment(self, name: str):
        self.counter[name] += 1

    def snapshot(self):
        return dict(self.counter)


metrics = Metrics()
