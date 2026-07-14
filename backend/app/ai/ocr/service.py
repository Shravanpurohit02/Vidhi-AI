from __future__ import annotations

from app.ai.integration.provider_router import provider_router

class OCRService:

    def extract(self, image, **kwargs):
        return provider_router.ocr(image=image, **kwargs)

    def vision(self, image, **kwargs):
        return provider_router.vision(image=image, **kwargs)
