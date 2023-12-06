import json
from fastapi import FastAPI

from chain import restaurant_agent
from parser import structure_output
from models import ReservationInput

from typing import Any
from langchain.schema.agent import AgentFinish
from langchain.callbacks.base import BaseCallbackHandler


app = FastAPI()


class CustomReservationHandler(BaseCallbackHandler):
    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        """This can be used to do extra post LLM agent if required"""
        pass


@app.post("/create_reservation/")
async def create_reservation(req: ReservationInput):
    """Mock POST API endpoint to run the agent/trigger the conversation and send a JSON"""
    # input_prompt = "Hi! I would like to make a table reservation for 4 people."

    restaurant_conversation = restaurant_agent.run(
        req.input_prompt, callbacks=[CustomReservationHandler()])
    json_result = json.loads(structure_output(restaurant_conversation))
    print(json_result) ## for logging purposes
    return json_result
