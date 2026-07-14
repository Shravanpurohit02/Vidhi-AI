import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.engineering.changeset import engine as ecs
from builder.engineering.state import engine as state


def main():

    change = ecs.create(
        objective="Engineering State Test",
        workspace=str(ROOT),
    )

    assert state.state.active_changeset == change.id
    assert state.state.current_objective == "Engineering State Test"

    ecs.complete(change)

    assert state.state.active_changeset == ""
    assert change.id in state.state.completed_changesets

    print("=" * 60)
    print("ENGINEERING STATE VERIFIED")
    print("=" * 60)
    print("ACTIVE     :", state.state.active_changeset)
    print("COMPLETED  :", len(state.state.completed_changesets))
    print("FAILED     :", len(state.state.failed_changesets))
    print("=" * 60)
    print("B-01.4.3 VERIFIED")


if __name__ == "__main__":
    main()
