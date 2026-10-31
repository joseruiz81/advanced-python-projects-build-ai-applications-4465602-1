import streamlit as st
from textblob import TextBlob
# Assuming you modularized your get_response function in CH_1_NLP_ChatBot.py
# from CH_1_NLP_ChatBot import get_response 

st.title("NLP Customer Service Chatbot")
st.write("Ask about our hours, returns, or grades!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call your NLP logic here
    # response = get_response(prompt) 
    response = "Happy to help! (This is where your intents response will go)"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
