from autogen_agentchat.agents import AssistantAgent
from prompts.planning_agent_prompt import PLANNING_AGENT_MESSAGE
from logger.logger import Logger

logger = Logger(__name__)

class PlanningAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def get_planning_agent(self):
        logger.info("Creating Planning Agent...")
        planning_agent = AssistantAgent(
            name="PlanningAgent",
            description="An agent for planning tasks, this agent should be the first to engage when given a new task.",
            model_client=self.model_client,
            system_message=PLANNING_AGENT_MESSAGE,
        )
        logger.info("Planning Agent created successfully.")
        return planning_agent

