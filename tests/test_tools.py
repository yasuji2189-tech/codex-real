import subprocess

def test_run_script():
    result = subprocess.run(["bash", "./tools/run.sh"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout

def test_check_script():
    result = subprocess.run(["bash", "./tools/check.sh"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout
    assert "hello, sasaki" in result.stdout
    assert "ok" in result.stdout
