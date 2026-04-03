import os
import subprocess

def test_help_still_works_with_env():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "nakamura"
    result = subprocess.run(["python", "main.py", "--help"], capture_output=True, text=True, check=True, env=env)
    assert "Simple greeting CLI" in result.stdout
