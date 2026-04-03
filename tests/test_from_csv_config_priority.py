import json
import subprocess
from pathlib import Path

def test_from_csv_beats_config_many_names():
    path = Path("data/priority_people.csv")
    path.write_text("name\nmori\nando\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-csv", str(path), "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, mori", "goodbye, ando"]

def test_from_csv_beats_config_default_name():
    path = Path("data/priority_single.csv")
    path.write_text("name\nyamada\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-csv", str(path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "goodbye, yamada" in result.stdout
