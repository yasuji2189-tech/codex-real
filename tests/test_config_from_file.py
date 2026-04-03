import json
import subprocess
from pathlib import Path

def test_config_with_from_file_uses_file_names():
    path = Path("data/config_file_names.txt")
    path.write_text("mori\nando\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-file", str(path), "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, mori", "goodbye, ando"]

def test_from_file_beats_config_many_names():
    path = Path("data/config_file_names_2.txt")
    path.write_text("ito\nkato\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-file", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "goodbye, ito" in result.stdout
    assert "goodbye, kato" in result.stdout
