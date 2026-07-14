from datetime import datetime

from builder.review.models import ReviewTask
from builder.review.storage import storage


class ReviewEngine:

    def list(self):
        return storage.load()

    def submit(self, improvement):

        tasks = storage.load()

        for task in tasks:

            if (
                task.target == improvement.target
                and task.issue == improvement.issue
                and task.status in (
                    "pending",
                    "approved",
                )
            ):
                return task

        task = ReviewTask(
            target=improvement.target,
            issue=improvement.issue,
            proposal=improvement.proposal,
            priority=improvement.priority,
        )

        tasks.append(task)

        storage.save(tasks)

        return task

    def approve(
        self,
        task_id: str,
        reviewer: str = "builder",
    ):

        tasks = storage.load()

        for task in tasks:

            if task.id == task_id:

                task.status = "approved"
                task.reviewer = reviewer
                task.reviewed_at = (
                    datetime.utcnow().isoformat()
                )

                storage.save(tasks)

                return task

        return None

    def reject(
        self,
        task_id: str,
        reviewer: str = "builder",
    ):

        tasks = storage.load()

        for task in tasks:

            if task.id == task_id:

                task.status = "rejected"
                task.reviewer = reviewer
                task.reviewed_at = (
                    datetime.utcnow().isoformat()
                )

                storage.save(tasks)

                return task

        return None


engine = ReviewEngine()
