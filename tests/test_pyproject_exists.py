from pathlib import Path

def test_pyproject_exists():
    text = Path("pyproject.toml").read_text(encoding="utf-8")
    assert 'name = "codex-real"' in text
    assert 'version = "0.1.1"' in text
    assert 'testpaths = ["tests"]' in text
