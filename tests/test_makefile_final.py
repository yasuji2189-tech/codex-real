from pathlib import Path

def test_makefile_final_targets():
    text = Path("Makefile").read_text(encoding="utf-8")
    assert "start:" in text
    assert "test:" in text
    assert "preflight:" in text
    assert "report:" in text
    assert "final-check:" in text
    assert "run-config:" in text
    assert "run-csv:" in text
