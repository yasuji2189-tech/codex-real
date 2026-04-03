import subprocess

def test_test_all_script():
    result = subprocess.run(
        ["bash", "./tools/test-all.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "passed" in result.stdout
