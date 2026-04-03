import subprocess

def test_version_script():
    result = subprocess.run(
        ["bash", "./tools/version.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "0.1.1" in result.stdout
