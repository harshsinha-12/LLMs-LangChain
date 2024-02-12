# main_script.py
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title('Your Personal Assistant, throw any question at me😉')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:')
    submitted = st.form_submit_button('Submit')

    if not text:
        st.warning('Please enter your text', icon='⚠')

    if submitted and text:
        generate_response(text)
