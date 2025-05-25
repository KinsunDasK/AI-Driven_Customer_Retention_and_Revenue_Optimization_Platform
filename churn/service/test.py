from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.environ.get("GROQ_API_KEY")
print(groq_api_key)

model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key, temperature = 0)

print(model.invoke("How are you"))