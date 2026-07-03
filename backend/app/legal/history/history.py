class ResearchHistory:

    def __init__(self):
        self.items = []

    def add(self, question: str, result: dict):
        self.items.append(
            {
                "question": question,
                "result": result,
            }
        )

    def all(self):
        return self.items

    def clear(self):
        self.items.clear()
