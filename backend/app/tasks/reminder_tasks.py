from app.jobs.job import Job
from app.workers.job_queue import queue


def enqueue_reminder(case_id: int):

    return queue.enqueue(
        Job(
            name="case_reminder",
            payload={
                "case_id": case_id,
            },
        )
    )
