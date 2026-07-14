from __future__ import annotations

class VisionEngine:

    def analyze(
        self,
        image,
    )->dict:

        raise NotImplementedError(
            "Vision provider not configured."
        )
