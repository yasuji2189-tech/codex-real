from src.config.settings import get_default_name, get_greeting_prefix

def greet(name=None):
    if name is None or name == "":
        name = get_default_name()
    return f"{get_greeting_prefix()}, {name}"

def greet_many(names):
    return [greet(name) for name in names]
