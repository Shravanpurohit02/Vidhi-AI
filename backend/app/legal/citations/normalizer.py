from __future__ import annotations

import re

class CitationNormalizer:

    @staticmethod
    def normalize(text:str)->str:
        return re.sub(r"\s+"," ",text).strip()
