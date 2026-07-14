from __future__ import annotations

from enum import StrEnum


class Capability(StrEnum):

    CHAT = "chat"
    EMBEDDING = "embedding"
    RERANK = "rerank"
    OCR = "ocr"
    VISION = "vision"
    IMAGE_GENERATION = "image_generation"
    FUNCTION_CALLING = "function_calling"
    SPEECH_TO_TEXT = "speech_to_text"
    TEXT_TO_SPEECH = "text_to_speech"
    MODERATION = "moderation"
