import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

sys.path.insert(0,str(ROOT/".builder"))

from builder.reflection.semantic_engine import engine

repo=engine.build(str(ROOT))

print("="*60)
print("MODULES :",len(repo.modules))
print("SYMBOLS :",len(repo.symbols))
print("="*60)

assert len(repo.modules)>0
assert len(repo.symbols)>0
