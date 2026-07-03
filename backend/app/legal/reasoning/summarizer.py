class JudgmentSummarizer:

    def summarize(self, text: str):

        words = text.split()

        return " ".join(words[:120])
