import subprocess

def test_main_default():
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True, check=True)
    assert "hello, world" in result.stdout

def test_main_name():
    result = subprocess.run(["python", "main.py", "sasaki"], capture_output=True, text=True, check=True)
    assert "hello, sasaki" in result.stdout
