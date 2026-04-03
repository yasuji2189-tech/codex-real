import subprocess

def test_run_many_script():
    result = subprocess.run(
        ["bash", "./tools/run-many.sh", "sasaki", "tanaka"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "hello, sasaki" in result.stdout
    assert "hello, tanaka" in result.stdout
