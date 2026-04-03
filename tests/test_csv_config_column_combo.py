import json
import subprocess
from pathlib import Path

def test_csv_custom_column_with_config_json():
    path = Path("data/combo_people.csv")
    path.write_text("person\nito\nkato\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-csv", str(path), "--csv-column", "person", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, ito", "goodbye, kato"]

def test_csv_custom_column_with_config_text():
    path = Path("data/combo_people_text.csv")
    path.write_text("person\nmori\nando\n", encoding="utf-8")
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--from-csv", str(path), "--csv-column", "person"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "goodbye, mori" in result.stdout
    assert "goodbye, ando" in result.stdout
