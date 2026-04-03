import json
import subprocess

def test_cli_many_overrides_config_many_names():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "--many", "ito", "kato", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(result.stdout) == ["goodbye, ito", "goodbye, kato"]

def test_cli_name_overrides_config_default_name():
    result = subprocess.run(
        ["python", "main.py", "--config", "config/sample.json", "yamada"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "goodbye, yamada" in result.stdout
