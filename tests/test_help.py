import subprocess

def test_help_output():
    result = subprocess.run(["python", "main.py", "--help"], capture_output=True, text=True, check=True)
    assert "Simple greeting CLI" in result.stdout
    assert "name to greet" in result.stdout
