import os
import subprocess

def test_many_default_prefix():
    result = subprocess.run(
        ["python", "main.py", "--many", "sasaki", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout

def test_many_env_prefix():
    env = os.environ.copy()
    env["APP_GREETING_PREFIX"] = "goodbye"
    result = subprocess.run(
        ["python", "main.py", "--many", "sasaki", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "goodbye, sasaki" in result.stdout
    assert "goodbye, tanaka" in result.stdout
