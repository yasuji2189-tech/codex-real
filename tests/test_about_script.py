import subprocess

def test_about_script():
    result = subprocess.run(
        ["bash", "./tools/about.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "app: codex-real" in result.stdout
    assert "version: 0.1.1" in result.stdout
