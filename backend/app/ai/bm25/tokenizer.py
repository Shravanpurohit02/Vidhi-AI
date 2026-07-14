from __future__ import annotations
import re

class BM25Tokenizer:

    @staticmethod
    def tokenize(text:str)->list[str]:
        return re.findall(r"[a-zA-Z0-9_]+", text.lower())
