from pathlib import Path

def test_verify_doc_exists():
    text = Path("docs/VERIFY.md").read_text(encoding="utf-8")
    assert "python main.py --version" in text
    assert "./tools/verify.sh" in text
