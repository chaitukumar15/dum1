
from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
# Load variables from .env file into the environment
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()


a=st.text_input("enter the text")
btn=st.button("submit")


if btn:
    with st.spinner("....loading"):
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
        )
    # print(response.text)
    st.markdown(response.text)