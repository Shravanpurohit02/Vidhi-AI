from app.jobs.job import Job
from app.workers.job_queue import queue


def enqueue_document_index(document_id: int):

    return queue.enqueue(
        Job(
            name="document_index",
            payload={
                "document_id": document_id,
            },
        )
    )
