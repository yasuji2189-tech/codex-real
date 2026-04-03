import json
import subprocess

def test_version_json_output():
    result = subprocess.run(
        ["python", "main.py", "--version", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "0.1.0"
