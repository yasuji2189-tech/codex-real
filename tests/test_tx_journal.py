import json
import subprocess

def test_tx_journal_text_output():
    result = subprocess.run(
        ["python", "main.py", "--tx-csv", "data/sample_transactions.csv", "--tx-journal"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "2026-04-01,消耗品費,1200,普通預金,1200,stationery,課税10%" in result.stdout
    assert "2026-04-02,旅費交通費,2500,普通預金,2500,taxi,課税10%" in result.stdout

def test_tx_journal_json_output():
    result = subprocess.run(
        ["python", "main.py", "--tx-csv", "data/sample_transactions.csv", "--tx-journal", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    data = json.loads(result.stdout)
    assert data[0]["debit_account"] == "消耗品費"
    assert data[1]["debit_account"] == "旅費交通費"
    assert data[0]["credit_account"] == "普通預金"
