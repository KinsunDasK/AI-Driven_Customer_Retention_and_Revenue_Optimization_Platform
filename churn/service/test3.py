from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import csv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

import pandas as pd

df = pd.read_csv(
    "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

groq_api_key = os.environ.get("GROQ_API_KEY")


model=ChatGroq(model="deepseek-r1-distill-llama-70b",groq_api_key=groq_api_key, temperature = 0)

#agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

agent = create_pandas_dataframe_agent(
    model,
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
     allow_dangerous_code=True
)

res = agent.invoke("how many rows are in the dataset")

print(res)