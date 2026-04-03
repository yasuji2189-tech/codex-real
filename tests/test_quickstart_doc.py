from pathlib import Path

def test_quickstart_doc_exists():
    text = Path("docs/QUICKSTART.md").read_text(encoding="utf-8")
    assert "python main.py --about" in text
    assert "./tools/about.sh" in text
