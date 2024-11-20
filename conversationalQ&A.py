import os
import requests
import streamlit as st

# Retrieve the API key from the environment variable
cohere_api_key = os.getenv("cohere_api_key")  # Ensure your API key is in the .env file

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat!")

# Initialize session state for chat messages if not already initialized
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        "You are a chatbot assistant with a sense of humor."
    ]

# Function to get response from Cohere API
def get_cohere_response(question):
    # Define the Cohere API endpoint
    url = "https://api.cohere.ai/v1/generate"
    
    # Set up the headers for authentication and content type
    headers = {
        "Authorization": f"Bearer {cohere_api_key}",
        "Content-Type": "application/json"
    }

    # Define the prompt for the API
    prompt = f"You are a chatbot assistant. Respond to the following question humorously: {question}"

    # Define the API payload
    payload = {
        "prompt": prompt,
        "max_tokens": 150,  # Limit to control the length of the response
        "temperature": 0.7  # Adjust the creativity of the response
    }

    # Send the POST request to Cohere API
    response = requests.post(url, headers=headers, json=payload)

    # Handle the response from the Cohere API
    if response.status_code == 200:
        result = response.json()
        return result['generations'][0]['text'].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Input field for user question
input_text = st.text_input("Input your question: ", key="input")

# Button to submit the question
if st.button("Ask the Question"):
    if input_text.strip():  # Check if the input is not empty
        response = get_cohere_response(input_text)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")
