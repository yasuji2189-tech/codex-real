import subprocess

def test_run_script():
    result = subprocess.run(["bash", "./tools/run.sh"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout

def test_clean_script():
    result = subprocess.run(["bash", "./tools/clean.sh"], capture_output=True, text=True, check=True)
    assert "cleaned" in result.stdout
