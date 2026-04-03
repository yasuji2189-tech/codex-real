import json
import subprocess

def test_about_text_output():
    result = subprocess.run(
        ["python", "main.py", "--about"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "app: codex-real" in result.stdout
    assert "version: 0.1.1" in result.stdout

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
