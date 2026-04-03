from pathlib import Path

def test_preflight_script_exists():
    text = Path("tools/preflight.sh").read_text(encoding="utf-8")
    assert "python main.py --version" in text
    assert "python main.py --about --json" in text
    assert "python main.py --config config/sample.json --json" in text
    assert "pytest -q" in text
