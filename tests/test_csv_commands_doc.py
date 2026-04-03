from pathlib import Path

def test_csv_commands_doc_exists():
    text = Path("docs/CSV_COMMANDS.md").read_text(encoding="utf-8")
    assert "python main.py --from-csv data/sample_names.csv" in text
    assert "--csv-column person" in text
    assert "--config config/sample.json" in text
