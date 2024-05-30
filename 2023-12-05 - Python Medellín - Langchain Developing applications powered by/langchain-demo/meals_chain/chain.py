from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import BaseOutputParser


class CommaSeparatedListOutputParser(BaseOutputParser[List[str]]):
    """Parse the output of an LLM call to a comma-separated list."""
    def parse(self, text: str) -> List[str]:
        """Parse the output of an LLM call."""
        return text.strip().split(", ")


template = """You are a helpful assistant who generates comma separated lists.
A user will pass in a country, and you should generate 20 food of that country in a comma separated list.
ONLY return a comma separated list, and nothing more."""

human_template = "{country}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_model = AzureChatOpenAI(deployment_name=  "GPT35-16k", model_name="gpt-35-turbo-16k")

chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()