import subprocess

def test_help_shows_about_option():
    result = subprocess.run(
        ["python", "main.py", "--help"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "--about" in result.stdout
