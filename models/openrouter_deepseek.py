from autogen_ext.models.openai import OpenAIChatCompletionClient
from logger.logger import Logger

logger = Logger(__name__)

class OpenRouterDeepSeekModelClient:
    def __init__(self, base_url, model, api_key, model_info):
        self.client = OpenAIChatCompletionClient(
            base_url=base_url,
            model=model,
            api_key=api_key,
            model_info=model_info
        )

    def get_model_client(self):
        logger.info("Initializing OpenRouter DeepSeek Model Client...")
        return self.client