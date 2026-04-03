import json
import subprocess

def test_from_csv_text_output():
    result = subprocess.run(
        ["python", "main.py", "--from-csv", "data/sample_names.csv"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout
    assert "hello, suzuki" in result.stdout

def test_from_csv_json_output():
    result = subprocess.run(
        ["python", "main.py", "--from-csv", "data/sample_names.csv", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["hello, sasaki", "hello, tanaka", "hello, suzuki"]
