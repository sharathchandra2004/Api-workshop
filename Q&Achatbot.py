# Q&A Chatbot using Cohere API

import streamlit as st
import cohere

# Initialize the Cohere client
COHERE_API_KEY = "COHERE_API_KEY"  # Replace with your actual API key
cohere_client = cohere.Client(COHERE_API_KEY)

# Function to get a response from the Cohere model
def get_cohere_response(question):
    response = cohere_client.generate(
        model="command-xlarge-2023",  # Use an appropriate model name
        prompt=question,
        max_tokens=100,  # Adjust as needed
        temperature=0.5
    )
    return response.generations[0].text.strip()

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application with Cohere API")

input_question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If the "Ask the question" button is clicked
if submit and input_question:
    st.subheader("The Response is")
    response = get_cohere_response(input_question)
    st.write(response)
