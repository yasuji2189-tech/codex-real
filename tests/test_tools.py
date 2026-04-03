import subprocess

def test_run_script():
    result = subprocess.run(["bash", "./tools/run.sh"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout

def test_test_script():
    result = subprocess.run(["bash", "./tools/test.sh"], capture_output=True, text=True, check=True)
    assert "passed" in result.stdout
