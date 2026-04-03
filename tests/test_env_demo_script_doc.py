from pathlib import Path

def test_env_demo_script_exists():
    text = Path("tools/env-demo.sh").read_text(encoding="utf-8")
    assert "APP_DEFAULT_NAME=tanaka python main.py" in text
    assert "APP_GREETING_PREFIX=goodbye python main.py sasaki" in text
    assert 'APP_DEFAULT_NAME=tanaka APP_GREETING_PREFIX=goodbye python main.py --many "" sasaki' in text
