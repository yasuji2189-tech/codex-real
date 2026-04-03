import json
import subprocess

def test_run_many_json_output():
    result = subprocess.run(
        ["python", "main.py", "--many", "sasaki", "tanaka", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["hello, sasaki", "hello, tanaka"]
