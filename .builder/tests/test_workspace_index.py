import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

sys.path.insert(0,str(ROOT/".builder"))

from builder.intelligence.workspace_index import workspace_indexer

idx=workspace_indexer.build(str(ROOT))

print("="*60)
print("MODULES :",idx.modules)
print("SYMBOLS :",idx.symbols)
print("IMPORTS :",idx.imports)
print("="*60)

assert idx.modules>0
assert idx.symbols>0
assert idx.imports>0
