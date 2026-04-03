import os
import subprocess

def test_main_many_with_empty_and_name():
    result = subprocess.run(
        ["python", "main.py", "--many", "", "sasaki"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, world" in result.stdout
    assert "hello, sasaki" in result.stdout

def test_main_many_with_env_default():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "nakamura"
    result = subprocess.run(
        ["python", "main.py", "--many", "", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "hello, nakamura" in result.stdout
    assert "hello, tanaka" in result.stdout
