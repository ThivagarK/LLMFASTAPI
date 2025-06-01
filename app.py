## streamlit for front-end
import streamlit as st
import requests
from dotenv import load_dotenv
import os

BASE_URL = "http://127.0.0.1:8000/generate"

# load environment variables
load_dotenv()

# Streamlit app to interact with the FastAPI backend
st.title("LLM Chat Bot")

# Create a prompt query for the LLM Chatbot
st.header("Create a prompt")
prompt=st.text_area("Prompt")
headers={"x-api-key": os.getenv("API_KEY"), "Content-Type": "application/json"}
if st.button("Submit"):
    response=requests.post(url=BASE_URL,json={"value":prompt}, headers=headers)
    st.write(response.json())