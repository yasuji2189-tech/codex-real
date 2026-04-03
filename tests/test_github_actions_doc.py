from pathlib import Path

def test_github_actions_workflow_exists():
    text = Path(".github/workflows/python-tests.yml").read_text(encoding="utf-8")
    assert "pytest -q" in text
    assert "actions/checkout@v4" in text
    assert "actions/setup-python@v5" in text
