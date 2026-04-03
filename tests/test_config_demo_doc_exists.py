from pathlib import Path

def test_config_demo_doc_exists():
    text = Path("docs/CONFIG_DEMO.md").read_text(encoding="utf-8")
    assert "./tools/config-demo.sh" in text
    assert "config many override" in text
    assert "config file input" in text
