import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Pro Application")
input = st.text_input("input: ", key="input" )   
submit= st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)
    

