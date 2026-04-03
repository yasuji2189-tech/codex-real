from pathlib import Path

def test_demo_doc_exists():
    text = Path("docs/DEMO.md").read_text(encoding="utf-8")
    assert "./tools/demo.sh" in text
    assert "single greeting" in text
