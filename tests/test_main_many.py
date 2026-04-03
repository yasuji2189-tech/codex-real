import subprocess

def test_main_single_name():
    result = subprocess.run(["python", "main.py", "sasaki"], capture_output=True, text=True, check=True)
    assert "hello, sasaki" in result.stdout

def test_main_default_name():
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout
