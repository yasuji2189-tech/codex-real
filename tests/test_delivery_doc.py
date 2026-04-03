from pathlib import Path

def test_delivery_doc_exists():
    text = Path("docs/DELIVERY.md").read_text(encoding="utf-8")
    assert "./tools/start.sh" in text
    assert "./tools/preflight.sh" in text
    assert "./tools/report.sh" in text
    assert "python main.py --from-csv data/sample_names.csv" in text
