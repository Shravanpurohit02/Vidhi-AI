from queue import Queue

from app.jobs.job import Job


class JobQueue:

    def __init__(self):
        self.queue: Queue[Job] = Queue()

    def enqueue(self, job: Job):
        self.queue.put(job)
        return job.id

    def dequeue(self):
        if self.queue.empty():
            return None
        return self.queue.get()

    def size(self):
        return self.queue.qsize()


queue = JobQueue()
