import subprocess
from pathlib import Path

def test_run_env_script_reads_env_file():
    env_file = Path(".env")
    old = env_file.read_text() if env_file.exists() else None
    try:
        env_file.write_text("APP_DEFAULT_NAME=yamada\n")
        result = subprocess.run(["bash", "./tools/run-env.sh"], capture_output=True, text=True, check=True)
        assert "hello, yamada" in result.stdout
    finally:
        if old is None:
            env_file.unlink(missing_ok=True)
        else:
            env_file.write_text(old)
