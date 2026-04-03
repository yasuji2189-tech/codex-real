import os

def get_default_name():
    return os.getenv("APP_DEFAULT_NAME", "world")
