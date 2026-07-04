from pathlib import Path

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
            parsed["text"],
            metadata,
        )

        parsed["status"] = "indexed"
        parsed["path"] = path
        parsed["metadata"] = metadata

        return parsed

    def ingest_directory(
        self,
        directory: str,
    ):
        directory = Path(directory)

        processed = []
        failed = []

        for file in directory.rglob("*"):

            if (
                not file.is_file()
                or file.suffix.lower() not in self.SUPPORTED_EXTENSIONS
            ):
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

        return {
            "documents": len(processed),
            "failed": len(failed),
            "files": processed,
            "failed_files": failed,
        }

    def statistics(
        self,
        directory: str,
    ):
        directory = Path(directory)

        files = [
            f
            for f in directory.rglob("*")
            if (
                f.is_file()
                and f.suffix.lower() in self.SUPPORTED_EXTENSIONS
            )
        ]

        return {
            "supported_extensions": sorted(
                self.SUPPORTED_EXTENSIONS
            ),
            "documents": len(files),
        }
