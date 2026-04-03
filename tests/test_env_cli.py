import os
import subprocess

def test_env_default_name():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "tanaka"
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True, check=True, env=env)
    assert "hello, tanaka" in result.stdout
