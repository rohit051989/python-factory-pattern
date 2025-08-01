

import os
import yaml
from functools import lru_cache


class Settings:
    """
    Loads application settings from a YAML config file based on the environment.
    """
    def __init__(self, config_path: str):
        """
        Initialize settings from a YAML file.
        :param config_path: Path to the YAML config file
        """
        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)
        self.app_name = cfg.get("app_name", "Enterprise FastAPI Template")
        self.debug = cfg.get("debug", True)
        self.database_url = cfg.get("database_url", "sqlite:///./test.db")
        self.llm_provider = cfg.get("llm_provider", "ollama")

@lru_cache()
def get_settings():
    """
    Get the application settings for the current environment.
    :return: Settings instance
    """
    env_name = os.getenv("ENV_NAME", "dev")
    config_path = os.path.join(os.path.dirname(__file__), f"config-{env_name}.yaml")
    return Settings(config_path)
