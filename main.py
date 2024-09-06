import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langfuse.callback import CallbackHandler

# langfuse initial setting
langfuse_handler = CallbackHandler(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

llm = ChatOpenAI()

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input": "how can langsmith help with testing?"}, config={"callbacks": [langfuse_handler]}))
