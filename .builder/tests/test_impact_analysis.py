import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.intelligence.impact import impact

result = impact.analyze(
    str(ROOT),
    "pathlib",
)

print("=" * 60)
print("TARGET   :", result["target"])
print("AFFECTED :", result["count"])
print("=" * 60)

assert result["count"] > 0
