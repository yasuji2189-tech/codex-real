from pathlib import Path

def test_config_verify_doc_exists():
    text = Path("docs/CONFIG_VERIFY.md").read_text(encoding="utf-8")
    assert "./tools/config-verify.sh" in text
    assert "config about json" in text
    assert "config version json" in text
