import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu


from langchain.agents import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import os
import time





load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")

st.set_page_config(
    page_title="Revenue_Performance_Optimization",
    layout="centered"
)





# main page title backgroung image
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://4kwallpapers.com/images/wallpapers/blue-aesthetic-2560x1440-16827.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)







st.markdown("""
    <style>
   /* Sidebar full panel with background image */
    .stSidebar {
        background-image: url("https://wallpapercave.com/wp/wp9418271.jpg");
        background-size: cover;
        background-position:55%  center;
        padding: 0px !important;
    }

    /* Sidebar inner content styling */
    .stSidebarContent {
        background-color: white !important;
        color: black !important;
        padding: 10px !important;
        border-radius: 0px;
    }
    </style>
    """, unsafe_allow_html=True)
# Sidebar with better selected option highlighting
with st.sidebar:
    st.markdown("""
    <div style='
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        padding: 10px 15px;
        border-radius: 8px;
        display: inline-block;
    '>
        <h3 style='color:white; margin: 0; font-style: italic; font-size: 25px;'>Navigation Menu</h3>
    </div>
    """, unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=['Predict Customer Churn', 'Revenue Optimization Chatbot'],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "white"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"color": "black", "font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {
                "background-color": "#D3D3D3",  # Light Gray highlight
                "color": "black",
                "font-weight": "bold"
            },
        }
    )





model = pickle.load(open("churn/pickles/model.pkl", "rb"))




########## Customer Churn Prediction ##########


if (selected == 'Predict Customer Churn'):



    st.markdown(
    """
    <style>
    .cus-title {
        font-size: 50px;
        color: #FF5733;
        font-family: 'Times New Roman', serif;
        font-weight: bold;
        font-style: italic;
        text-align: center;
        margin-bottom: 30px;
    }
    .custom-header {
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 30px;
        color: #2E86C1;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        text-decoration: underline;
    }
    </style>
    <h1 class="cus-title">Revenue Performance Optimization by Predicting Customer Churn</h1>
    <h2 class="custom-header">Provide Customer Details for Prediction</h2>
    """,
    unsafe_allow_html=True
    )







    st.markdown("""
    <style>
    /* Style the dropdown container */
    div[data-baseweb="select"] > div {
        background-color: #f0f8ff !important;
        border: 2px solid black !important;
        border-radius: 10px !important;
        padding: 0px !important;
    }

    /* Style the dropdown placeholder and selected value */
    div[data-baseweb="select"] > div > div {
        color: black !important;
        font-weight: bold !important;
        font-size: 14px !important;
    }

    /* Style the options menu */
    div[role="listbox"] {
        background-color: #f0f8ff !important;
        border: 2px solid #4B0082 !important;
        border-radius: 0px !important;
    }

    /* Style individual options */
    div[role="option"] {
        color: black !important;
        padding: 8px !important;
    }
    
    /* Style the arrow (caret) */
    div[data-baseweb="select"] svg {
    color: black !important;
    fill: black !important;
    }

    /* Style number input box */
    input[type=number] {
        background-color: #f0f8ff !important;
        color: black !important;
        border: 2px solid black !important;
        border-radius: 10px !important;
        padding: 8px !important;
        font-size: 16px !important;
    }

    /* Shared label styling */
    label {
        font-weight: bold !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)



    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        gender = {"Male": 1, "Female": 0}.get(st.selectbox("gender", ["Male", "Female"]))
        SeniorCitizen = {"yes": 1, "no": 0}.get(st.selectbox("SeniorCitizen", ["yes", "no"]))
        Partner = {"Yes": 1, "No": 0}.get(st.selectbox("Partner", ["Yes", "No"]))
        Dependents = {"Yes": 1, "No": 0}.get(st.selectbox("Dependents", ["Yes", "No"]))
    
    with col2:
        tenure = st.number_input("Tenure", min_value=0, value =1)
        PhoneService = {"Yes": 1, "No": 0}.get(st.selectbox("PhoneService", ["Yes", "No"]))
        MultipleLines = {"Yes": 2, "No": 0, "No phone service": 1}.get(st.selectbox("MultipleLines", ["Yes", "No","No phone service"]))   
        InternetService = {"Fiber optic": 1, "DSL": 0, "No": 2}.get(st.selectbox("InternetService", ["Fiber optic", "DSL","No"]))
    
    with col3:
        OnlineSecurity = {"No": 0, "Yes": 2, "No internet service": 1}.get(st.selectbox("OnlineSecurity", ["No", "Yes", "No internet service"]))   
        OnlineBackup = {"No": 0, "Yes": 2, "No internet service": 1}.get(st.selectbox("OnlineBackup", ["No", "Yes", "No internet service"]))      
        DeviceProtection  = {"No": 0, "Yes": 2, "No internet service": 1}.get(st.selectbox("DeviceProtection", ["No", "Yes", "No internet service"]))  
        TechSupport = {"No": 0, "Yes": 2, "No internet service": 1}.get(st.selectbox("TechSupport", ["No", "Yes", "No internet service"]))     
    
    with col4:
        StreamingTV = {"No": 0, "Yes": 2, "No internet service": 1}.get(st.selectbox("StreamingTV", ["No", "Yes", "No internet service"]))
        StreamingMovies = {"Yes": 1, "No": 0}.get(st.selectbox("StreamingMovies", ["Yes", "No"]))
        Contract = {"Month-to-month": 0, "One year": 2, "Two year": 1}.get(st.selectbox("Contract", ["Month-to-month", "One year", "Two year"]))
        PaperlessBilling = {"Yes": 1, "No": 0}.get(st.selectbox("PaperlessBilling", ["Yes", "No"]))
    
    with col5:
        PaymentMethod = {"Electronic check": 2, "Mailed check": 3, "Bank transfer": 0,"Credit card":1}.get(st.selectbox("PaymentMethod", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])) 
        MonthlyCharges = st.number_input("MonthlyCharges", min_value=0.0, value = 29.5)
        TotalCharges = st.number_input("TotalCharges",  min_value=0.0, value = 29.5)

    if st.button("Predict"):
        input_data = pd.DataFrame(
                {
                    "gender": [gender],
                    "SeniorCitizen": [SeniorCitizen],
                    "Partner": [Partner],
                    "Dependents": [Dependents],
                    "tenure": [tenure],        
                    "PhoneService": [PhoneService],
                    "MultipleLines": [MultipleLines],
                    "InternetService": [InternetService],
                    "OnlineSecurity": [OnlineSecurity],
                    "OnlineBackup": [OnlineBackup],
                    "DeviceProtection": [DeviceProtection],
                    "TechSupport": [TechSupport],
                    "StreamingTV": [StreamingTV],
                    "StreamingMovies": [StreamingMovies],
                    "Contract": [Contract],
                    "PaperlessBilling": [PaperlessBilling],
                    "PaymentMethod": [PaymentMethod],
                    "MonthlyCharges": [MonthlyCharges],
                    "TotalCharges": [TotalCharges]
                    
                })

        #st.write(input_data)

        prediction = model.predict(input_data)

            
        with st.spinner('Analyzing customer behavior...'):
            time.sleep(1)

            # Dynamic Result Display
            if prediction[0] == 0:
                st.markdown("""
                    <div style='text-align: center; padding: 20px; border: 3px solid green; border-radius: 10px; background-color: #e6ffe6;'>
                    <h2 style='color: green;'>✅ The Customer is Likely to Stay!</h2>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='text-align: center; padding: 20px; border: 3px solid red; border-radius: 10px; background-color: #ffe6e6;'>
                <h2 style='color: red;'>⚠️ The Customer is Likely to Churn!</h2>
                </div>
                """, unsafe_allow_html=True)







########## Chatbot ##########

if (selected == 'Revenue Optimization Chatbot'):
    st.title('Revenue Optimization Chatbot')



    
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Initialize DataFrame
    if "df" not in st.session_state:
        st.session_state.df = None

    # Load dataset
    file_path = "churn/datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    if file_path:
        st.session_state.df = pd.read_csv(file_path)

    st.markdown("""
    <style>
    [data-testid="stChatMessageAvatar"] {
        display: flex !important;
    }
    [data-testid="stChatMessage"] {
        flex-direction: row-reverse !important;
    }
    
    [data-testid="stChatMessage"] {
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
        padding: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)


    # Display chat history with styled bubbles
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(f"""
                <div style='display: flex; justify-content: flex-end;'>
                <div style='
                    background: rgba(0, 0, 0, 0.7);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    backdrop-filter: blur(10px);
                    -webkit-backdrop-filter: blur(10px);
                    border-radius: 15px;
                    padding: 15px 20px;
                    color: white;
                    max-width: 70%;
                    box-shadow: 0 8px 32px 0 rgba( 255, 255, 255, 0.37 );
                    text-align: left;'>
                    {message['content']}
                    </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
               st.markdown(f"""
                <div style='display: flex; justify-content: flex-start;'>
                <div style='
                    background: rgba(0, 0, 0, 0.7);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    backdrop-filter: blur(10px);
                    -webkit-backdrop-filter: blur(10px);
                    border-radius: 15px;
                    padding: 15px 20px;
                    color: white;
                    max-width: 70%;
                    box-shadow: 0 8px 32px 0 rgba( 255, 255, 255, 0.37 );
                    text-align: left;'>
                    {message['content']}
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    # User input
    user_prompt = st.chat_input("Ask your queries...")

    if user_prompt:
        # Show user message with bubble style
        st.markdown(f"""
                <div style='display: flex; justify-content: flex-end;'>
                <div style='
                    background: rgba(0, 0, 0, 0.7);
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    backdrop-filter: blur(10px);
                    -webkit-backdrop-filter: blur(10px);
                    border-radius: 15px;
                    padding: 15px 20px;
                    color: white;
                    max-width: 70%;
                    box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
                    text-align: left;'>
                    {user_prompt}
                </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        # Load model and agent
        model = ChatGroq(model="deepseek-r1-distill-llama-70b", groq_api_key=groq_api_key, temperature=0)

        pandas_df_agent = create_pandas_dataframe_agent(
            model,
            st.session_state.df,
            verbose=True,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            allow_dangerous_code=True
        )

        # Prepare system message and chat history
        messages = [
            {"role": "system", "content": (
                "You are an expert data analyst specialized in Revenue Performance Optimization. "
                "Your task is to analyze the provided pandas DataFrame and answer the user's questions accurately and concisely. "
                "When presenting numerical results, please round to two decimal places unless otherwise specified. "
                "If the user requests to modify or write the data, do not do it and only provide analysis-related answers. "
                "If the user asks for a summary, provide a brief overview of the key findings. "
                "Do not show any Python scripts. Provide only strict answers without a preamble."
            )},
            *st.session_state.chat_history
        ]

        # Get LLM Response
        response = pandas_df_agent.invoke(messages)
        assistant_response = response["output"]

        # Save and show assistant response with bubble style
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(f"""
                <div style='background-color: rgba(0, 0, 0, 0.7); 
                    padding: 10px 15px; 
                    border-radius: 10px; 
                    color: white; 
                    display: inline-block;'>
                    {assistant_response}
                </div>
                """, unsafe_allow_html=True)