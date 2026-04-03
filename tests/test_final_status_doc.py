from pathlib import Path

def test_final_status_doc_exists():
    text = Path("docs/FINAL_STATUS.md").read_text(encoding="utf-8")
    assert "single input" in text
    assert "csv input" in text
    assert "./tools/report.sh" in text
    assert "python main.py --help" in text
