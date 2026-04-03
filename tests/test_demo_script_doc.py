from pathlib import Path

def test_demo_script_exists():
    text = Path("tools/demo.sh").read_text(encoding="utf-8")
    assert 'python main.py --about' in text
    assert 'python main.py --version' in text
