import os
import subprocess

def test_combined_env_changes_output():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "tanaka"
    env["APP_GREETING_PREFIX"] = "goodbye"
    result = subprocess.run(
        ["python", "main.py"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "goodbye, tanaka" in result.stdout

def test_combined_env_many_output():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "tanaka"
    env["APP_GREETING_PREFIX"] = "goodbye"
    result = subprocess.run(
        ["python", "main.py", "--many", "", "sasaki"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "goodbye, tanaka" in result.stdout
    assert "goodbye, sasaki" in result.stdout
