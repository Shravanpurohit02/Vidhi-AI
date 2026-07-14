from __future__ import annotations

from app.document_processing.ocr.ocr_engine import OCREngine
from app.document_processing.ocr.vision_engine import VisionEngine


class OCRService:

    def __init__(self):

        self.ocr=OCREngine()
        self.vision=VisionEngine()

    def process(
        self,
        image,
    ):

        return {
            "text":self.ocr.extract(image),
            "vision":self.vision.analyze(image),
        }
