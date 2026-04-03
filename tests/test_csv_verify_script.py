from pathlib import Path

def test_csv_verify_script_exists():
    text = Path("tools/csv-verify.sh").read_text(encoding="utf-8")
    assert "python main.py --from-csv data/sample_names.csv" in text
    assert "python main.py --from-csv data/sample_names.csv --json" in text
    assert "python main.py --from-csv data/sample_names.csv --about --json" in text
    assert "python main.py --from-csv data/sample_names.csv --version --json" in text
