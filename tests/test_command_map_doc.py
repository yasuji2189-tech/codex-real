from pathlib import Path

def test_command_map_doc_exists():
    text = Path("docs/COMMAND_MAP.md").read_text(encoding="utf-8")
    assert "python main.py --about" in text
    assert "./tools/demo.sh" in text
    assert "./tools/verify.sh" in text
