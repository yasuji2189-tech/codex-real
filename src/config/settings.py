import os

def get_default_name():
    return os.getenv("APP_DEFAULT_NAME", "world")

def get_greeting_prefix():
    return os.getenv("APP_GREETING_PREFIX", "hello")
