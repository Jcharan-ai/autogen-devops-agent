from autogen_agentchat.agents import AssistantAgent
from prompts.deployer_agent_prompt import DEPLOYER_AGENT_PROMPT
from logger.logger import Logger

logger = Logger(__name__)

class DeployerAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def get_deployer_agent(self):
        logger.info("Creating Deployer Agent...")
        deployer_agent = AssistantAgent(
            name="DeployerAgent",
            description="An agent for deployment tasks, this agent should be responsible for the deployment details.",
            model_client=self.model_client,
            system_message=DEPLOYER_AGENT_PROMPT,
        )
        logger.info("Deployer Agent created successfully.")
        return deployer_agent

