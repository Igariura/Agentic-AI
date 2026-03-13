from strands import Agent
import logging

# Add debug logging to see what your agent is thinking
logging.basicConfig(level=logging.DEBUG)

# Create the agent with the system prompt
agent = Agent(
    system_prompt="You are a game master for a Dungeon & Dragon game"
)

# Summon your agent with a basic incantation
response = agent("Hi, I am an adventurer ready for adventure!")
print(response)