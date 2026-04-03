from src.config.settings import DEFAULT_NAME

def greet(name=None):
    if name is None:
        name = DEFAULT_NAME
    return f'hello, {name}'
