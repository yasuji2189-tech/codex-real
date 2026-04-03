from pathlib import Path

def test_env_vars_doc_exists():
    text = Path("docs/ENV_VARS.md").read_text(encoding="utf-8")
    assert "APP_DEFAULT_NAME" in text
    assert "APP_GREETING_PREFIX" in text
    assert "goodbye" in text
