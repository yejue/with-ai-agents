from pydantic import BaseModel, Field

BaseModel.model_config["protected_namespaces"] = ()


class Config:
    def __init__(
            self,
            api_key: str = None,
            platform: str = None,
            model_name: str = None,
            tavily_api_key: str = None
    ):
        self.api_key = api_key
        self.platform = platform
        self.model_name = model_name
        self.tavily_api_key = tavily_api_key


def get_config():
    from with_ai_agents import api_key, platform, model_name, tavily_api_key

    config_instance = Config(
        api_key=api_key,
        platform=platform,
        model_name=model_name,
        tavily_api_key=tavily_api_key
    )
    return config_instance
