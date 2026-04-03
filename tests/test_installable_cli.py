import json
import subprocess

def test_main_wrapper_still_works():
    result = subprocess.run(["python", "main.py", "--version"], capture_output=True, text=True, check=True)
    assert "0.1.1" in result.stdout

def test_module_cli_works():
    result = subprocess.run(["python", "-m", "src.cli", "--version"], capture_output=True, text=True, check=True)
    assert "0.1.1" in result.stdout
