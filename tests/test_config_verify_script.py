from pathlib import Path

def test_config_verify_script_exists():
    text = Path("tools/config-verify.sh").read_text(encoding="utf-8")
    assert "python main.py --config config/sample.json" in text
    assert "python main.py --config config/sample.json yamada --json" in text
    assert "python main.py --config config/sample.json --about --json" in text
    assert "python main.py --config config/sample.json --version --json" in text
