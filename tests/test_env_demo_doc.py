from pathlib import Path

def test_env_demo_doc_exists():
    text = Path("docs/ENV_DEMO.md").read_text(encoding="utf-8")
    assert "./tools/env-demo.sh" in text
    assert "combined default + prefix demo" in text
