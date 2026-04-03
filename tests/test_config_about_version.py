import json
import subprocess

def test_about_with_config_json_output():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--about", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(result.stdout)
    assert data["app"] == "codex-real"
    assert data["version"] == "0.1.1"

def test_version_with_config_json_output():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--version", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "0.1.1"
