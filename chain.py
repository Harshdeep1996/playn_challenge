from datetime import datetime

from langchain.tools import Tool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType, load_tools


# instantiate the GPT-4 model
LLM = ChatOpenAI(model="gpt-4", temperature=0)

## Define a new tool that returns the current datetime
datetime_tool = Tool(
    name="Datetime check",
    func=lambda x: datetime.now().date(),
    description="Returns the current datetime",
)

## List of tools which can be added
## https://python.langchain.com/docs/integrations/tools/human_tools
internal_tools = load_tools(["human"])
TOOLS = internal_tools + [datetime_tool]

## Memory for the conversation so that 3 parameters
MEMORY = ConversationBufferMemory(memory_key="memory", return_messages=True)

PREFIX = """
You are a restaurant table reservation agent at John Baker and would like to know the date, time and number of people of a reservation.
Get the current date in YYYY-MM-DD format using tool and put the date given by the user in this format.
You need to have access to all these 3 information before you close the conversation.
You have access to the following tools:
"""
SUFFIX = """Begin!

Question: {input}
Thought:{agent_scratchpad}"""

## Initialize the agent with the new tool
## Using Zero shot react - reasons before it acts and update the new prompt with persona
restaurant_agent = initialize_agent(
    TOOLS,
    LLM,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=MEMORY,
    max_iterations=5,
    agent_kwargs={"prefix": PREFIX, "suffix": SUFFIX}
)
