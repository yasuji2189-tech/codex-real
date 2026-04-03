import subprocess

def test_version_output():
    result = subprocess.run(["python", "main.py", "--version"], capture_output=True, text=True, check=True)
    assert "0.1.1" in result.stdout
