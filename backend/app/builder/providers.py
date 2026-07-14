import sys

from .runtime import BUILDER_ROOT

builder_path = str(BUILDER_ROOT.resolve())

if builder_path not in sys.path:
    sys.path.insert(0, builder_path)
