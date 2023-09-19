"""Settings module"""
import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="pamps",
    preload=[os.path.join(HERE, "default.toml")],
    environments=["development", "production", "testing"],
    env_switcher="pamps_env",
    load_dotenv=False,
)
