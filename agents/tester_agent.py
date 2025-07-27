from autogen_agentchat.agents import AssistantAgent
from prompts.tester_agent_prompt import TESTER_AGENT_MESSAGE
from logger.logger import Logger

logger = Logger(__name__)

class TesterAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def get_tester_agent(self):
        logger.info("Creating Tester Agent...")
        tester_agent = AssistantAgent(
            name="TesterAgent",
            description="An agent for testing tasks, this agent should be responsible for ensuring the quality and reliability of the software.",
            model_client=self.model_client,
            system_message=TESTER_AGENT_MESSAGE,
        )
        logger.info("Tester Agent created successfully.")
        return tester_agent

