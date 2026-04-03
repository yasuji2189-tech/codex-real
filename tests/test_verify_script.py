import subprocess

def test_verify_script_runs():
    result = subprocess.run(
        ["bash", "./tools/verify.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "0.1.1" in result.stdout
    assert "app: codex-real" in result.stdout
    assert "passed" in result.stdout
