from src.config.settings import get_default_name

def test_default_name_exists():
    value = get_default_name()
    assert isinstance(value, str)
    assert len(value) >= 1
