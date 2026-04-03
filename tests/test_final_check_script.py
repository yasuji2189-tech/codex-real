from pathlib import Path

def test_final_check_script_exists():
    text = Path("tools/final-check.sh").read_text(encoding="utf-8")
    assert "python main.py --help" in text
    assert "python main.py --version" in text
    assert "python main.py --about --json" in text
    assert "python main.py --config config/sample.json --json" in text
    assert "python main.py --from-csv data/sample_names.csv --json" in text
    assert "pytest -q" in text
    assert "git status" in text
