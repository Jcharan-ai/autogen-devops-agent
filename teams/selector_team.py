from autogen_agentchat.conditions import TextMentionTermination,MaxMessageTermination
from autogen_agentchat.teams import SelectorGroupChat
from prompts.selector_prompt import SELECTOR_PROMPT
from logger.logger import Logger

logger = Logger(__name__)

class SelectorTeam:
    def __init__(self, model_client, planning_agent, user_proxy_agent, deployer_agent, builder_agent, tester_agent):
        self.model_client = model_client
        self.planning_agent = planning_agent
        self.user_proxy_agent = user_proxy_agent
        self.deployer_agent = deployer_agent
        self.builder_agent = builder_agent
        self.tester_agent = tester_agent

    def get_selector_team(self):
        logger.info("Creating Selector Team...")
        selector_team = SelectorGroupChat(
            participants=[self.planning_agent, self.user_proxy_agent, self.deployer_agent, self.builder_agent, self.tester_agent],
            model_client=self.model_client,
            termination_condition=self.get_termination_conditions(),
            selector_prompt=SELECTOR_PROMPT,
            allow_repeated_speaker=True
        )
        logger.info("Selector Team created successfully.")
        
        return selector_team
    
    def get_termination_conditions(self):
        text_mention_termination = TextMentionTermination('TERMINATE')
        max_message_termination = MaxMessageTermination(max_messages=20)
        combined_termination = text_mention_termination | max_message_termination
        
        return combined_termination
