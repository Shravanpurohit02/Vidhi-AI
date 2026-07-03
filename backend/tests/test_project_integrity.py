from pathlib import Path

REQUIRED_FILES = [
    "app/main.py",
    "app/core/config.py",
    "app/core/logging.py",
    "app/database/database.py",
    "app/database/init_db.py",
    "app/models/user.py",
    "app/repositories/user_repository.py",
    "app/services/user_service.py",
    "app/auth/security.py",
    "app/auth/password.py",
    "app/auth/dependencies.py",
    "app/api/v1/users.py",
    "app/api/v1/auth.py",
    "app/api/v1/profile.py",
]


def test_required_project_files_exist():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} is missing"
