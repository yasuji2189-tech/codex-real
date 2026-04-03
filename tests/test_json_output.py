import json
import subprocess

def test_main_json_single():
    result = subprocess.run(
        ["python", "main.py", "sasaki", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "hello, sasaki"

def test_main_json_many():
    result = subprocess.run(
        ["python", "main.py", "--many", "sasaki", "tanaka", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["hello, sasaki", "hello, tanaka"]
