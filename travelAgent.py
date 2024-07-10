import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv
import time


load_dotenv()

open_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=open_api_key)

tools = load_tools(['ddg-search','wikipedia'], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

query = """
Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com os eventos que irão ocorrer na data da viagem e com o preço da passagem de São Paulo para Londres.
"""

agent.run(query)