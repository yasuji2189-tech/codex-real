from pathlib import Path

def test_license_exists():
    text = Path("LICENSE").read_text(encoding="utf-8")
    assert "MIT License" in text
    assert "Permission is hereby granted" in text
