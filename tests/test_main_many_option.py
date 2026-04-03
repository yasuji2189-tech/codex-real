import subprocess

def test_main_many_option():
    result = subprocess.run(
        ["python", "main.py", "--many", "sasaki", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout
