import json
import subprocess

def test_config_file_json_output():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, sasaki", "goodbye, suzuki"]

def test_config_file_version_still_works():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "0.1.1" in result.stdout
