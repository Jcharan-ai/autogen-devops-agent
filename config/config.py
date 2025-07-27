from dotenv import load_dotenv
from logger.logger import Logger
import os

load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
LANGSMITH_PROJECT="autogen-devops-agent"
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"

logger = Logger(__name__)
logger.info("Configuration in progress...")

OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "deepseek/deepseek-r1-0528-qwen3-8b:free"

logger.info("Configuration completed successfully.")
