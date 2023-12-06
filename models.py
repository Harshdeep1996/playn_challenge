from typing import Optional
from pydantic import BaseModel
from langchain.pydantic_v1 import BaseModel as BM, Field


class ReservationRecord(BM):
    """
    Pydantic model for storing the reservation records.

    https://github.com/langchain-ai/langchain/blob/50aee687c60ec3ca5be0887a696e30ca3200ec31/libs/langchain/langchain/utils/openai_functions.py#L26
    """
    date: str = Field(description="The date at which reservation takes place")
    time: str = Field(description="The time at which reservation takes place")
    num_people: int = Field(description="The number of people who will attend the reservation")


class ReservationInput(BaseModel):
    """
    Pydantic model for starting the conversation with a input prompt.
    """
    input_prompt: str
