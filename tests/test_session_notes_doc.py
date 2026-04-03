from pathlib import Path

def test_session_notes_doc_exists():
    text = Path("docs/SESSION_NOTES.md").read_text(encoding="utf-8")
    assert "wsl" in text
    assert "./tools/start.sh" in text
