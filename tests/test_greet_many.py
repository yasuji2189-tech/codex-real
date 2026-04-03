from src.app import greet_many

def test_greet_many_basic():
    assert greet_many(["sasaki", "tanaka"]) == ["hello, sasaki", "hello, tanaka"]

def test_greet_many_empty():
    assert greet_many([]) == []
