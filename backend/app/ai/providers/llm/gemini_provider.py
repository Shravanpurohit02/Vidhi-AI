from __future__ import annotations

import os

import google.generativeai as genai

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class GeminiProvider(AIProvider):

    name = "gemini"

    priority = 3

    capabilities = {
        Capability.CHAT,
        Capability.EMBEDDING,
        Capability.VISION,
        Capability.OCR,
    }

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GOOGLE_API_KEY"),
        )

    def health(self) -> bool:
        return bool(os.getenv("GOOGLE_API_KEY"))

    def chat(
        self,
        prompt: str,
        model: str = "gemini-2.5-pro",
    ):

        m = genai.GenerativeModel(model)

        return m.generate_content(prompt)

    def vision(
        self,
        prompt,
        image,
        model: str = "gemini-2.5-pro",
    ):

        m = genai.GenerativeModel(model)

        return m.generate_content(
            [prompt, image],
        )

    def ocr(self, image):
        return self.vision(
            "Extract all readable text from this document.",
            image,
        )
