from src.app import greet

def test_greet_none_uses_default():
    assert greet(None) == "hello, world"

def test_greet_empty_uses_default():
    assert greet("") == "hello, world"
