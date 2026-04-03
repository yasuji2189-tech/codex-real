from src.config.settings import DEFAULT_NAME

def greet(name=None):
    if name is None or name == "":
        name = DEFAULT_NAME
    return f"hello, {name}"

def greet_many(names):
    return [greet(name) for name in names]
