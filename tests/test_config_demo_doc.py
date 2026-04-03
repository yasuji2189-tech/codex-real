from pathlib import Path

def test_config_demo_script_exists():
    text = Path("tools/config-demo.sh").read_text(encoding="utf-8")
    assert "python main.py --config config/sample.json" in text
    assert "python main.py --config config/sample.json --many ito kato --json" in text
    assert "python main.py --config config/sample.json --from-file data/names.txt --json" in text
