import os
import random
import streamlit as st
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

def initialize_session_state():
    """
    Initialize the session state variables if they don't exist.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []


def display_customization_options():
    """
    Add customization options to the sidebar for model selection and memory length.
    """
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)
    return model, conversational_memory_length

def initialize_groq_chat(groq_api_key, model):
    """
    Initialize the Groq Langchain chat object.
    """
    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )

def initialize_conversation(groq_chat, memory):
    """
    Initialize the conversation chain with the Groq chat object and memory.
    """
    return ConversationChain(
        llm=groq_chat,
        memory=memory
    )

def process_user_question(user_question, conversation):
    """
    Process the user's question and generate a response using the conversation chain.
    """
    response = conversation(user_question)
    message = {'human': user_question, 'AI': response['response']}
    st.session_state.chat_history.append(message)
    st.write("Chatbot:", response['response'])

def main():
    """
    The main entry point of the application.
    """
    groq_api_key = os.environ['GROQ_API_KEY']

    initialize_session_state()

    st.title("Chat with a lightning fast AI chatbot!")
    st.write("Hello! I'm your friendly groq-powered chatbot named Lightning. I can help answer your questions, provide information, or just chat. I'm also super fast! Let's start our conversation!")

    model, conversational_memory_length = display_customization_options()
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    user_question = st.text_input("Ask a question:")

    for message in st.session_state.chat_history:
        memory.save_context({'input': message['human']}, {'output': message['AI']})

    groq_chat = initialize_groq_chat(groq_api_key, model)
    conversation = initialize_conversation(groq_chat, memory)

    if user_question:
        process_user_question(user_question, conversation)

if __name__ == "__main__":
    main()