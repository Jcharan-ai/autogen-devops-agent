from autogen_agentchat.agents import UserProxyAgent
from logger.logger import Logger

logger = Logger(__name__)

class DuserProxyAgent:
   
    def get_user_proxy_agent(self):
        logger.info("Creating User Proxy Agent...")
        user_proxy_agent = UserProxyAgent(
            name='UserProxy',
            description='you are a user proxy agent',
            input_func=input
        )
        logger.info("User Proxy Agent created successfully.")
        return user_proxy_agent

