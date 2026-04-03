import os
import subprocess

def test_about_default_still_works():
    result = subprocess.run(
        ["python", "main.py", "--about"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "app: codex-real" in result.stdout
    assert "version: 0.1.1" in result.stdout

def test_prefix_does_not_break_about():
    env = os.environ.copy()
    env["APP_GREETING_PREFIX"] = "goodbye"
    result = subprocess.run(
        ["python", "main.py", "--about"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "app: codex-real" in result.stdout
    assert "version: 0.1.1" in result.stdout
