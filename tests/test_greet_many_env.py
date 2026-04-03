import os

def test_greet_many_respects_env_default():
    old = os.environ.get("APP_DEFAULT_NAME")
    os.environ["APP_DEFAULT_NAME"] = "nakamura"
    try:
        from importlib import reload
        import src.config.settings as settings
        import src.app as app
        reload(settings)
        reload(app)
        assert app.greet_many([None, "sasaki"]) == ["hello, nakamura", "hello, sasaki"]
    finally:
        if old is None:
            os.environ.pop("APP_DEFAULT_NAME", None)
        else:
            os.environ["APP_DEFAULT_NAME"] = old
