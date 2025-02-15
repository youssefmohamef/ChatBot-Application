
import streamlit as st
import google.generativeai as genai

api = 'AIzaSyD7RBmXPFcgU8wrIZ_ZOWqVaOXTycSqjmw'

st.title('Google AI Text Generation')

if api:
    genai.configure(api_key=api)
else:
    st.error("Your API is Not Valid")

def Generate_Text(text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text

if 'messages' not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if user_input := st.chat_input('Enter Your Text ...'):
    with st.chat_message('user'):
        st.markdown(user_input)

    st.session_state.messages.append({'role':'user','content':user_input})

    with st.chat_message('assistant'):
        message_placehoder = st.empty()
        with st.spinner('Generating Response ...'):
            response_text = Generate_Text(user_input)
            message_placehoder.markdown(f'{response_text}')
        st.session_state.messages.append({'role':'assistant','content':response_text})
