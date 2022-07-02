from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from subprocess import CompletedProcess, run
from typing import List, Optional, Union

__all__ = ["Task", "run_tasks_concurently", "run_task"]


@dataclass(frozen=True)
class Task:
    """
    Uses shell if `executable` is not provided.
    See:
    * https://docs.python.org/3/library/subprocess.html#subprocess.run
    * https://docs.python.org/3/library/subprocess.html#subprocess.Popen
    """
    parameters: List[Union[Path, str]]
    executable: Optional[Path] = None


def run_tasks_concurently(tasks: List[Task]) -> List[CompletedProcess]:
    with ProcessPoolExecutor() as executor:
        return list(executor.map(run_task, tasks))


def run_task(task: Task) -> CompletedProcess:
    return run(
        executable=task.executable,
        args=task.parameters,
        capture_output=True,
    )
