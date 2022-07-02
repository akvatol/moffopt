from task_runner import Task, run_task, run_tasks_concurently


def test_run_task():

    parameters = ["echo", "hello world"]

    task = Task(parameters=parameters)
    completed_process  = run_task(task)

    assert completed_process.args == parameters
    assert completed_process.returncode == 0

    assert completed_process.stdout == b"hello world\n"
    assert completed_process.stderr == b""


def test_run_tasks_concurently():

    tasks = [
        Task(parameters=["echo", "hello"]),
        Task(parameters=["echo", "world"]),
    ]
    completed_processes = run_tasks_concurently(tasks)

    assert len(completed_processes) == len(tasks)
    assert completed_processes[0].stdout == b"hello\n"
    assert completed_processes[1].stdout == b"world\n"
