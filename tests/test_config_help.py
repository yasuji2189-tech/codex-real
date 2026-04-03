import subprocess

def test_help_shows_config_option():
    result = subprocess.run(
        ["python", "main.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "--config" in result.stdout
