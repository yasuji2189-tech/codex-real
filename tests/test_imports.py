from src.app import greet
from src.config.settings import get_default_name

def test_imports():
    assert get_default_name() == "world"
    assert greet() == "hello, world"
