from autogen_agentchat.agents import AssistantAgent
from prompts.builder_agent_prompt import BUILDER_AGENT_MESSAGE
from logger.logger import Logger

logger = Logger(__name__)

class BuilderAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def get_builder_agent(self):
        logger.info("Creating Builder Agent...")
        builder_agent = AssistantAgent(
            name="BuilderAgent",
            description="An agent for building tasks, this agent should be responsible for the implementation details.",
            model_client=self.model_client,
            system_message=BUILDER_AGENT_MESSAGE,
        )
        logger.info("Builder Agent created successfully.")
        return builder_agent

