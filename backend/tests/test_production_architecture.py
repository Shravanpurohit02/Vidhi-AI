from pathlib import Path

REQUIRED_FILES = [
    "app/jobs/job.py",
    "app/workers/job_queue.py",
    "app/tasks/document_tasks.py",
    "app/tasks/email_tasks.py",
    "app/tasks/reminder_tasks.py",
    "app/security/api_key.py",
    "app/monitoring/metrics.py",
    "app/audit/audit_log.py",
    "app/api/v1/jobs.py",
    "app/api/v1/system.py",
    "Dockerfile",
    "docker-compose.yml",
    "Makefile",
    ".env.example",
    "alembic.ini",
]


def test_production_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
