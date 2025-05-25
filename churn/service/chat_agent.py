import pandas as pd
import streamlit as st
from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import csv
import os

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")
# streamlit web app configuration
st.set_page_config(
    page_title="Revenue_Performance_Optimization",
    page_icon="💬",
    layout="centered"
)


def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)


# streamlit page title
st.title("🤖 Revenue Optimization ChatBot")

# initialize chat history in streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# initiate df iin session state
if "df" not in st.session_state:
    st.session_state.df = None


# file upload widget
file_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
#file_path = "holidays_events.csv"

if file_path:
    st.session_state.df = pd.read_csv(file_path)
    #st.write("DataFrame Preview:")
    #st.dataframe(st.session_state.df.head())


# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message
user_prompt = st.chat_input("Ask your queries...")

if user_prompt:
    # add user's message to chat history and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content": user_prompt})

    # loading the LLM
    model=ChatGroq(model="deepseek-r1-distill-llama-70b",groq_api_key=groq_api_key, temperature = 0)

    pandas_df_agent = create_pandas_dataframe_agent(
        model,
        st.session_state.df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        allow_dangerous_code=True
    )

    messages = [
        {"role":"system", "content": "You are an expert data analyst. Your task is to analyze the provided pandas DataFrame and answer the user's questions accurately and concisely. "
        "When presenting numerical results, please round to two decimal places unless otherwise specified. "
        "If the user asks for a summary, provide a brief overview of the key findings.Dont show nay python scripts. Only strict answers and not preamble."},
        *st.session_state.chat_history
    ]

    response = pandas_df_agent.invoke(messages)

    assistant_response = response["output"]

    st.session_state.chat_history.append({"role":"assistant", "content": assistant_response})

    # display LLM response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

