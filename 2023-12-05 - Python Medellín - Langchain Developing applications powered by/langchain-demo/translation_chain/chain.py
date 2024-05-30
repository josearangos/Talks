
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

translation_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

llm = ChatOpenAI(model_name="gpt-3.5-turbo-1106")

chain = translation_prompt | llm
