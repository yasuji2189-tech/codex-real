from pathlib import Path

def test_prefix_demo_script_exists():
    text = Path("tools/prefix-demo.sh").read_text(encoding="utf-8")
    assert "APP_GREETING_PREFIX=goodbye python main.py sasaki" in text
    assert "APP_GREETING_PREFIX=goodbye python main.py --many sasaki tanaka" in text
