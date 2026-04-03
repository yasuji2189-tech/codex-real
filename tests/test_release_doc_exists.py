from pathlib import Path

def test_release_doc_exists():
    text = Path("docs/RELEASE.md").read_text(encoding="utf-8")
    assert "0.1.0" in text
    assert "python main.py --version" in text
