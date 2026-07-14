from __future__ import annotations

from enum import Enum


class CitationStyle(str, Enum):
    SCC = "scc"
    AIR = "air"
    NEUTRAL = "neutral"
    RAW = "raw"
