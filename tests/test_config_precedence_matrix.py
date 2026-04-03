import json
import subprocess
from pathlib import Path

def test_precedence_config_then_name():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "yamada", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "goodbye, yamada"

def test_precedence_config_then_many():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--many", "ito", "kato", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, ito", "goodbye, kato"]

def test_precedence_config_then_file():
    path = Path("data/precedence_names.txt")
    path.write_text("mori\nando\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-file", str(path), "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, mori", "goodbye, ando"]
