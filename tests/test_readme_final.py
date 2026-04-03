from pathlib import Path

def test_readme_final_contains_key_commands():
    text = Path("README.md").read_text(encoding="utf-8")
    assert "python main.py --from-csv data/sample_names.csv" in text
    assert "python main.py --config config/sample.json" in text
    assert "./tools/final-check.sh" in text
    assert "0.1.1" in text
