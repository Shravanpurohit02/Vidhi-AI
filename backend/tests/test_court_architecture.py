from pathlib import Path


REQUIRED_FILES = [
    "app/models/cause_list.py",
    "app/models/court_schedule.py",
    "app/models/litigation_timeline.py",
    "app/services/dashboard_service.py",
    "app/legal/drafting/drafting_service.py",
    "app/legal/templates/templates.py",
    "app/automation/reminder_service.py",
    "app/analytics/case_analytics.py",
    "app/workflows/workflow_service.py",
    "app/api/v1/dashboard.py",
    "app/api/v1/drafting.py",
    "app/api/v1/workflow.py",
]


def test_court_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
