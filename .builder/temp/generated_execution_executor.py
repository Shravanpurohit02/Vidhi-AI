# builder/execution/executor.py

from builder import (
    config_manager,
    context,
    logger,
    models,
    queue,
    runtime,
    settings,
    tasks,
    telemetry,
    types,
    typing,
    uuid,
)
from builder.exceptions import ExecutorError
from builder.models import ExecutionRequest, ExecutionResponse
from builder.queue import ExecutionQueue
from builder.runtime import RuntimeEnvironment
from builder.telemetry import TelemetryClient
from pydantic import BaseModel

class Executor(BaseModel):
    """Executor responsible for executing tasks."""

    queue: ExecutionQueue
    runtime_env: RuntimeEnvironment
    telemetry_client: TelemetryClient
    config: settings.ExecutorConfig

    def __init__(self, **kwargs):
        """Initialize executor with dependencies."""
        self.queue = queue.ExecutionQueue()
        self.runtime_env = runtime.RuntimeEnvironment()
        self.telemetry_client = telemetry.TelemetryClient()
        self.config = settings.ExecutorConfig(**config_manager.get_executor_config())

    async def execute(self, request: ExecutionRequest) -> ExecutionResponse:
        """Execute a task based on the execution request."""
        try:
            # Fetch task from the queue
            task = tasks.get_task(request.task_id)
            if not task:
                raise ExecutorError(f"Task {request.task_id} not found")

            # Prepare execution environment
            env = self.runtime_env.prepare_environment(task.requirements)

            # Execute the task
            result = await task.execute(env, **request.params)

            # Log execution result
            logger.execution_logger.info(
                f"Task {request.task_id} executed successfully",
                task_id=request.task_id,
                result=result,
            )

            # Send telemetry event
            self.telemetry_client.send_event(
                "task_executed",
                task_id=request.task_id,
                status="success",
            )

            return ExecutionResponse(
                task_id=request.task_id,
                result=result,
                status="success",
            )

        except Exception as e:
            # Handle execution failure
            logger.execution_logger.error(
                f"Task {request.task_id} execution failed",
                task_id=request.task_id,
                error=str(e),
            )

            self.telemetry_client.send_event(
                "task_executed",
                task_id=request.task_id,
                status="failure",
                error=str(e),
            )

            raise ExecutorError(f"Task execution failed: {str(e)}") from e

    async def run(self):
        """Run the executor, processing tasks from the queue."""
        while True:
            request: ExecutionRequest = await self.queue.get_next_task()
            if not request:
                await context.sleep(self.config.idle_sleep_seconds)
                continue

            try:
                response = await self.execute(request)
                await self.queue.task_completed(response)
            except ExecutorError as e:
                await self.queue.task_failed(request, str(e))
                logger.execution_logger.error(
                    "Executor error processing task",
                    task_id=request.task_id,
                    error=str(e),
                )

def get_executor() -> Executor:
    """Factory function to get an instance of the Executor."""
    return Executor()