from pathlib import Path

from app.document_processing import DocumentProcessingService
from app.jobs.job import Job
from app.workers.job_queue import queue


class DocumentTasks:

    processor = DocumentProcessingService()

    @classmethod
    def process_uploaded_document(
        cls,
        document,
    ):
        path = Path(document.file_path)

        if not path.exists():
            return {
                "status": "missing_file",
            }

        try:
            text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )
        except Exception:
            text = ""

        return cls.processor.process(
            document_id=document.id,
            text=text,
        )


def enqueue_document_index(document):
    """
    Backward-compatible API.
    Always enqueue a job so the existing Jobs subsystem
    continues to function.
    """

    job = Job(name="document_index")

    queue.enqueue(job)

    if isinstance(document, int):
        return job.id

    try:
        DocumentTasks.process_uploaded_document(document)
    except Exception:
        pass

    return job.id
