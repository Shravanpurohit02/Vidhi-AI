import py_compile
import shutil
from pathlib import Path


class Applier:

    def apply(self, path, code):

        target = Path(path)

        if not target.exists():
            return {
                "success": False,
                "reason": "Target file not found.",
            }

        backup = target.with_suffix(
            target.suffix + ".bak"
        )

        shutil.copy2(target, backup)

        try:

            target.write_text(
                code,
                encoding="utf-8",
            )

            py_compile.compile(
                str(target),
                doraise=True,
            )

            backup.unlink(missing_ok=True)

            return {
                "success": True,
                "path": str(target),
            }

        except Exception as exc:

            shutil.copy2(backup, target)
            backup.unlink(missing_ok=True)

            return {
                "success": False,
                "path": str(target),
                "reason": str(exc),
                "rolled_back": True,
            }


applier = Applier()
