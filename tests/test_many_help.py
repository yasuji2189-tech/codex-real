import subprocess

def test_help_shows_many_option():
    result = subprocess.run(["python", "main.py", "--help"], capture_output=True, text=True, check=True)
    assert "--many" in result.stdout
