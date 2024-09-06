from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

llm = ChatOpenAI()

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"input": "how can langsmith help with testing?"}))
