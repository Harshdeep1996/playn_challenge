import asyncio
import langchain_visualizer
from chain import restaurant_agent


async def restaurant_agent_visualize():
    """Running the agent with a prompt as a async function"""
    return restaurant_agent.run(
        "Hi! I would like to make a table reservation tomorrow for 4 people.")

langchain_visualizer.visualize(restaurant_agent_visualize)
