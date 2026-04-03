from pathlib import Path

def test_handoff_doc_exists():
    text = Path("docs/HANDOFF.md").read_text(encoding="utf-8")
    assert "./tools/start.sh" in text
    assert "./tools/final-check.sh" in text
    assert "make run-config" in text
    assert "make run-csv" in text
