import json
import subprocess

def test_transactions_csv_text_output():
    result = subprocess.run(
        ["python", "main.py", "--tx-csv", "data/sample_transactions.csv"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "2026-04-01,stationery,1200" in result.stdout
    assert "2026-04-02,taxi,2500" in result.stdout

def test_transactions_csv_json_output():
    result = subprocess.run(
        ["python", "main.py", "--tx-csv", "data/sample_transactions.csv", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(result.stdout)
    assert data[0]["date"] == "2026-04-01"
    assert data[0]["description"] == "stationery"
    assert data[0]["amount"] == 1200
