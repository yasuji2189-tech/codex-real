import json
import subprocess

def test_about_json_output():
    result = subprocess.run(
        ["python", "main.py", "--about", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(result.stdout)
    assert data["app"] == "codex-real"
    assert data["version"] == "0.1.1"
