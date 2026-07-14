from __future__ import annotations

from pathlib import Path
from time import perf_counter

from app.ai.services.ai_service import AIService
from app.legal.parsers.legal_parser import LegalParser


class KnowledgeBase:

    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".md",
        ".pdf",
        ".docx",
    }

    def __init__(self):
        self.ai = AIService()
        self.parser = LegalParser()

    def ingest_file(
        self,
        path: str,
        metadata: dict | None = None,
    ):

        metadata = metadata or {}

        parsed = self.parser.parse(path)

        self.ai.ingest_document(
            text=parsed["text"],
            metadata=metadata,
        )

        parsed["status"] = "indexed"
        parsed["path"] = path
        parsed["metadata"] = metadata

        return parsed

    def ingest_directory(
        self,
        directory: str,
    ):

        started = perf_counter()

        directory_path = Path(directory)

        processed: list[str] = []
        failed: list[str] = []
        skipped: list[str] = []

        total = 0

        for file in directory_path.rglob("*"):

            if not file.is_file():
                continue

            total += 1

            if file.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                skipped.append(str(file))
                continue

            try:

                self.ingest_file(
                    str(file),
                    {
                        "filename": file.name,
                        "path": str(file),
                    },
                )

                processed.append(str(file))

            except Exception:
                failed.append(str(file))

        elapsed = perf_counter() - started

        return {
            "documents": len(processed),
            "indexed": len(processed),
            "failed": len(failed),
            "skipped": len(skipped),
            "scanned": total,
            "processing_time": elapsed,
            "files": processed,
            "failed_files": failed,
            "skipped_files": skipped,
        }

    def statistics(
        self,
        directory: str,
    ):

        directory_path = Path(directory)

        files = [
            f
            for f in directory_path.rglob("*")
            if (f.is_file() and f.suffix.lower() in self.SUPPORTED_EXTENSIONS)
        ]

        return {
            "supported_extensions": sorted(
                self.SUPPORTED_EXTENSIONS,
            ),
            "documents": len(files),
        }
