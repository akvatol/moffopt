from process import Process, execute_process, execute_processes_concurently


def test_execute_process():

    parameters = ["echo", "hello world"]

    process = Process(args=parameters)
    completed_process  = execute_process(process)

    assert completed_process.args == parameters
    assert completed_process.returncode == 0

    assert completed_process.stdout == "hello world\n"
    assert completed_process.stderr == ""


def test_execute_processes_concurently():

    parameters = [
        Process(args=["echo", "hello"]),
        Process(args=["echo", "world"]),
    ]
    completed_processes = execute_processes_concurently(parameters)

    assert completed_processes[0].stdout == "hello\n"
    assert completed_processes[1].stdout == "world\n"
