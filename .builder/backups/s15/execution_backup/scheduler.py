from builder.core.jobs import jobs

class Scheduler:

    def next_job(self):
        items = jobs.all()
        for job in items:
            if job.status == "pending":
                return job
        return None

scheduler = Scheduler()
