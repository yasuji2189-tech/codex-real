from pathlib import Path

def test_next_steps_doc_exists():
    text = Path("docs/NEXT_STEPS.md").read_text(encoding="utf-8")
    assert "CLI works" in text
    assert "add CI workflow" in text
