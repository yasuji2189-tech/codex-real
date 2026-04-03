from src.app import greet_many

def test_greet_many_uses_default_for_none():
    assert greet_many([None, "sasaki"]) == ["hello, world", "hello, sasaki"]

def test_greet_many_uses_default_for_empty():
    assert greet_many(["", "tanaka"]) == ["hello, world", "hello, tanaka"]
