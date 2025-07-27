SELECTOR_PROMPT = '''
Select an agent to perform the task. 
First you should select the planning agent to assign a task, then other agents can work on it.

{roles}

current conversation history :
{history}

Read the above conversation, then select an agent from {participants} to perform the next task.
Make sure that the planning agent has assigned task before other agents start working.
Only select one agent.
'''