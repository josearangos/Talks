from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_toolkits import GmailToolkit
from langchain.agents import AgentExecutor
from langchain.pydantic_v1 import BaseModel
from langchain.memory import ConversationBufferMemory


db = SQLDatabase.from_uri("sqlite:///resources/users.db")
db_toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))


gmail_toolkit = GmailToolkit()

llm=ChatOpenAI(temperature=0,model_name="gpt-4")

tools = gmail_toolkit.get_tools()+db_toolkit.get_tools()

agent = initialize_agent(
    llm=llm,
    tools=tools,
    verbose=False,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

class AgentInputs(BaseModel):
    input: str

agent_executor = agent.with_types(input_type=AgentInputs) 
