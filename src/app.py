from src.config.settings import get_default_name

def greet(name=None):
    if name is None or name == "":
        name = get_default_name()
    return f"hello, {name}"

def greet_many(names):
    return [greet(name) for name in names]
