import json
import os
import subprocess

def test_json_single_default():
    result = subprocess.run(
        ["python", "main.py", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "hello, world"

def test_json_single_env_default():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "nakamura"
    result = subprocess.run(
        ["python", "main.py", "--json"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert json.loads(result.stdout) == "hello, nakamura"

def test_json_many_env_default():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "nakamura"
    result = subprocess.run(
        ["python", "main.py", "--many", "", "tanaka", "--json"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert json.loads(result.stdout) == ["hello, nakamura", "hello, tanaka"]
