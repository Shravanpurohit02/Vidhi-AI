from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

BUILDER_ROOT = PROJECT_ROOT / ".builder"

BUILDER_PACKAGE = BUILDER_ROOT / "builder"

STATE = BUILDER_ROOT / "state"
CACHE = BUILDER_ROOT / "cache"
LOGS = BUILDER_ROOT / "logs"
RUNTIME = BUILDER_ROOT / "runtime"
