from pathlib import Path

def test_prefix_demo_doc_exists():
    text = Path("docs/PREFIX_DEMO.md").read_text(encoding="utf-8")
    assert "./tools/prefix-demo.sh" in text
    assert "json env prefix greeting" in text
