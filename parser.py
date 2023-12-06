import pydantic
from typing import Optional

from models import ReservationRecord

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains.openai_functions import create_structured_output_runnable


LLM = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


def structure_output(processed_input: str) -> Optional[dict]:
    """
    Structure the output of the model using a Pydantic model and prompt.

    :params: processed_input: conversational input from the user about the 3 params.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an algorithm to extract information in JSON/Pydantic format."),
            ("human", "Use the given format to extract information from the following processed input: {input}"),
            ("human", "Make sure to answer in the correct format as provided."),
        ]
    )

    runnable = create_structured_output_runnable(ReservationRecord, LLM, prompt)
    try:
        resp = runnable.invoke({"input": processed_input})
        return resp.json()
    except pydantic.v1.error_wrappers.ValidationError as e:
        print("The information was not supplied in the right format.") 


if __name__ == "__main__":
    print(structure_output("need a reservation 2023-12-07 at 8:30 PM for 4"))
