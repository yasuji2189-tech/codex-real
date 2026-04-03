from pathlib import Path

def test_project_summary_doc_exists():
    text = Path("docs/PROJECT_SUMMARY.md").read_text(encoding="utf-8")
    assert "single greeting" in text
    assert "python main.py --about" in text
