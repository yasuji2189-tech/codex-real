import json
import os
import subprocess

def test_json_default_prefix():
    result = subprocess.run(
        ["python", "main.py", "sasaki", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "hello, sasaki"

def test_json_env_prefix():
    env = os.environ.copy()
    env["APP_GREETING_PREFIX"] = "goodbye"
    result = subprocess.run(
        ["python", "main.py", "sasaki", "--json"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert json.loads(result.stdout) == "goodbye, sasaki"
