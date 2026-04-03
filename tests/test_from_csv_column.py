import json
import subprocess
from pathlib import Path

def test_from_csv_custom_column_text():
    path = Path("data/people.csv")
    path.write_text("person\nsasaki\ntanaka\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--from-csv", str(path), "--csv-column", "person"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout

def test_from_csv_custom_column_json():
    path = Path("data/people_json.csv")
    path.write_text("person\nsasaki\ntanaka\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--from-csv", str(path), "--csv-column", "person", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["hello, sasaki", "hello, tanaka"]
