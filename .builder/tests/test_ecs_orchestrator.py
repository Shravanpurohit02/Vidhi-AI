import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.engineering.changeset import engine as ecs


def main():

    changeset = ecs.create(
        objective="Orchestrator Integration",
        workspace=str(ROOT),
    )

    assert changeset.objective == "Orchestrator Integration"
    assert changeset.repository.project == "Vidhi-AI"
    assert len(changeset.repository.modules) > 0

    print("=" * 60)
    print("ENGINEERING CHANGE SET")
    print("=" * 60)
    print("ID       :", changeset.id)
    print("PROJECT  :", changeset.repository.project)
    print("MODULES  :", len(changeset.repository.modules))
    print("STATUS   :", changeset.status)
    print("=" * 60)
    print("B-01.3 VERIFIED")


if __name__ == "__main__":
    main()
