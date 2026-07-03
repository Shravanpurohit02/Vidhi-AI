from textwrap import wrap


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        overlap: int = 200,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str):

        if not text:
            return []

        chunks = []

        step = max(
            1,
            self.chunk_size - self.overlap,
        )

        for i in range(
            0,
            len(text),
            step,
        ):
            chunks.append(
                text[i:i+self.chunk_size]
            )

        return chunks
