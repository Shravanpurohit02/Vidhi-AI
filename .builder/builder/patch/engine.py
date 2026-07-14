import tempfile
import py_compile
from pathlib import Path

from builder.patch.applier import applier
from builder.patch.diff import diff_engine
from builder.patch.models import Patch
from builder.patch.validator import validator


class PatchEngine:

    def create(
        self,
        path: str,
        updated: str,
    ):

        original = Path(path).read_text(
            encoding="utf-8",
            errors="ignore",
        )

        return Patch(
            path=path,
            original=original,
            updated=updated,
        )

    def preview(
        self,
        patch: Patch,
    ):
        return diff_engine.diff(
            patch.original,
            patch.updated,
        )

    def validate(
        self,
        patch: Patch,
    ):
        patch.validated = validator.validate(
            patch.updated,
        )
        return patch.validated

    def compile(
        self,
        patch: Patch,
    ):

        fd, tmp = tempfile.mkstemp(suffix=".py")

        try:
            Path(tmp).write_text(
                patch.updated,
                encoding="utf-8",
            )

            py_compile.compile(
                tmp,
                doraise=True,
            )

            patch.compiled = True

        finally:
            Path(tmp).unlink(
                missing_ok=True,
            )

        return patch.compiled

    def commit(
        self,
        patch: Patch,
    ):

        if not self.validate(patch):
            raise RuntimeError(
                "Patch validation failed."
            )

        if not self.compile(patch):
            raise RuntimeError(
                "Patch compilation failed."
            )

        applier.apply(
            patch.path,
            patch.updated,
        )

        patch.committed = True

        return patch

    def rollback(
        self,
        patch: Patch,
    ):

        applier.apply(
            patch.path,
            patch.original,
        )

        patch.rolled_back = True

        return patch


engine = PatchEngine()
