import streamlit as st
from langchain_ollama import ChatOllama

st.title('ChatBot')

def generate(text):
    model = ChatOllama(
        model='llama3.2:1b',
        base_url='http://localhost:11434/'
    )

    response = model.invoke(text)

    return response.content

with st.form("my_form"):
    text = st.text_area("Enter your question")
    submitted = st.form_submit_button("Submit")

if submitted and text:
    response = generate(text)
    st.session_state['history'].append({'user': text, 'ollama': response})
    st.write(response)


if 'history' not in st.session_state:
    st.session_state['history'] = []

st.title('History')
for chat in st.session_state['history']:
    st.write(chat['user'])
    st.write(chat['ollama'])
    st.write('****')