import platform
import sys
from pathlib import Path

from builder.project import analyzer
from builder.reflection import query

from .manifest import RuntimeManifest
from .runtime import Runtime

class RuntimeInspector:

    def inspect(self):
        runtime = Runtime(
            project=Path.cwd().name,
            workspace=str(Path.cwd()),
            python=sys.version.split()[0],
            platform=platform.platform(),
        )

        summary = analyzer.summary()

        manifest = RuntimeManifest(
            files=summary["files"],
            modules=len(query.functions()) + len(query.classes()),
            classes=len(query.classes()),
            functions=len(query.functions()),
        )

        return runtime, manifest

inspector = RuntimeInspector()
