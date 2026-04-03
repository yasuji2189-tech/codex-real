from src.app import greet
from src.config.settings import DEFAULT_NAME

def test_imports():
    assert DEFAULT_NAME == "world"
    assert greet() == "hello, world"
