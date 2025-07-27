import asyncio

from models.openrouter_deepseek import OpenRouterDeepSeekModelClient
from config.config import BASE_URL, MODEL_NAME, OPEN_ROUTER_API_KEY
from agents.planning_agent import PlanningAgent
from agents.deployer_agent import DeployerAgent
from agents.builder_agent import BuilderAgent
from agents.tester_agent import TesterAgent
from agents.user_proxy_agent import DuserProxyAgent
from teams.selector_team import SelectorTeam
from autogen_agentchat.ui import Console
from logger.logger import Logger

logger = Logger(__name__)

async def main():
    # Initialize agents with OpenAI model clients.
    base_url = BASE_URL
    model = MODEL_NAME
    api_key = OPEN_ROUTER_API_KEY
    model_info = {
        "family": 'deepseek',
        "vision": True,
        "function_calling": True,
        "json_output": False
    }
    model_client = OpenRouterDeepSeekModelClient(base_url, model, api_key, model_info).get_model_client()
    planning_agent = PlanningAgent(model_client)
    deployer_agent = DeployerAgent(model_client)
    builder_agent = BuilderAgent(model_client)
    tester_agent = TesterAgent(model_client)
    user_proxy_agent = DuserProxyAgent()
    selector_team = SelectorTeam(
        model_client=model_client,
        planning_agent=planning_agent.get_planning_agent(),
        user_proxy_agent=user_proxy_agent.get_user_proxy_agent(),
        deployer_agent=deployer_agent.get_deployer_agent(),
        builder_agent=builder_agent.get_builder_agent(),
        tester_agent=tester_agent.get_tester_agent()
    ).get_selector_team()
    task = "Please plan and automate a full CI/CD pipeline for a Python web app."
    #while True:
        
        # Run the team and print the events.
    await Console(selector_team.run_stream(task=task))
    
        #feedback_from_user_or_application=input('Please Provide feedback to the team: ')

        #if(feedback_from_user_or_application.lower().strip()=='exit'):
        #    break

        #task = feedback_from_user_or_application


if __name__ == "__main__":
    # Run the main function in an event loop.
    logger.info("Starting the DevOps Agent...")
    asyncio.run(main())
    logger.info("DevOps Agent started successfully.")



