from src.config.settings import DEFAULT_NAME

def test_default_name_exists():
    assert isinstance(DEFAULT_NAME, str)
    assert len(DEFAULT_NAME) >= 1
