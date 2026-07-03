from app.jobs.job import Job
from app.workers.job_queue import queue


def enqueue_email(email: str, subject: str):

    return queue.enqueue(
        Job(
            name="send_email",
            payload={
                "email": email,
                "subject": subject,
            },
        )
    )
