from dataclasses import dataclass
from pathlib import Path
import os
import platform
import sys

@dataclass(slots=True)
class Environment:
    os_name: str
    platform_name: str
    python_version: str
    cwd: Path
    home: Path
    termux: bool

    @classmethod
    def detect(cls) -> "Environment":
        prefix = os.environ.get("PREFIX", "")
        return cls(
            os_name=os.name,
            platform_name=platform.platform(),
            python_version=sys.version.split()[0],
            cwd=Path.cwd(),
            home=Path.home(),
            termux="com.termux" in prefix,
        )
