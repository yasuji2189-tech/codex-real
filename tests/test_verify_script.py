import pathlib

def test_verify_script_file_exists():
    text = pathlib.Path("tools/verify.sh").read_text(encoding="utf-8")
    assert "python main.py --version" in text
    assert "python main.py --about" in text
    assert "pytest -q" in text
