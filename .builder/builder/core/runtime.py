from builder.filesystem import scanner
from builder.models.runtime import RuntimeContext
from builder.core.recovery import recovery

runtime = RuntimeContext()
runtime.project = scanner.scan(runtime.workspace)

recovery.recover()
