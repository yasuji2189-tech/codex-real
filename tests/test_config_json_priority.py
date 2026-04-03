import json
import subprocess

def test_config_json_flag_applies_without_cli_json():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert isinstance(json.loads(result.stdout), list)

def test_cli_json_still_works_with_config_and_name():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "yamada", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == "goodbye, yamada"
