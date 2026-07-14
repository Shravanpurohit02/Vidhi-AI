from .models import EngineeringState


class StateEngine:

    def __init__(self):

        self._state = EngineeringState()

    @property
    def state(self):
        return self._state

    def activate(
        self,
        changeset_id,
        objective,
    ):
        self._state.active_changeset = changeset_id
        self._state.current_objective = objective

    def complete(
        self,
        changeset_id,
    ):
        if changeset_id not in self._state.completed_changesets:
            self._state.completed_changesets.append(
                changeset_id
            )

        if self._state.active_changeset == changeset_id:
            self._state.active_changeset = ""
            self._state.current_objective = ""

    def fail(
        self,
        changeset_id,
    ):
        if changeset_id not in self._state.failed_changesets:
            self._state.failed_changesets.append(
                changeset_id
            )


engine = StateEngine()
