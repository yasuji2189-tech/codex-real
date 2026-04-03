import os
import subprocess

def test_run_many_script_with_default():
    result = subprocess.run(
        ["bash", "./tools/run-many.sh", "", "sasaki"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, world" in result.stdout
    assert "hello, sasaki" in result.stdout

def test_run_many_script_with_env_default():
    env = os.environ.copy()
    env["APP_DEFAULT_NAME"] = "nakamura"
    result = subprocess.run(
        ["bash", "./tools/run-many.sh", "", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    assert "hello, nakamura" in result.stdout
    assert "hello, tanaka" in result.stdout
