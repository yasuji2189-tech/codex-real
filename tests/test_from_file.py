import json
import subprocess
from pathlib import Path

def test_from_file_text_output():
    path = Path("data/test_names.txt")
    path.write_text("sasaki\ntanaka\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--from-file", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout

def test_from_file_json_output():
    path = Path("data/test_names_json.txt")
    path.write_text("sasaki\ntanaka\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--from-file", str(path), "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["hello, sasaki", "hello, tanaka"]
