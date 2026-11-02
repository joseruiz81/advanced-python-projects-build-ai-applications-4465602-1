import streamlit as st

# 1. Import the function from your existing file
from CH_1_NLP_ChatBot import get_response

st.title("Mulgrave Customer Service Chatbot (testing jruiz)")
st.write("Ask about our address, contact, hours, or grades")
st.write("sentiment-based responses for a chatbot using TextBlob")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Pass the user's prompt to your existing get_response function
    response = get_response(prompt) 

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
