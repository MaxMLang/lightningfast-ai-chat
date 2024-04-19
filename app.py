import os
import streamlit as st
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

def initialize_session_state():
    """
    Initialize the session state variables if they don't exist.
    """
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'model' not in st.session_state:
        st.session_state.model = 'llama3-8b-8192'

def display_customization_options():
    """
    Add customization options to the sidebar for model selection and memory length.
    """
    st.sidebar.title('Customization')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['llama3-8b-8192','mixtral-8x7b-32768', 'llama2-70b-4096'],
        key='model_selectbox'
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

def main():
    """
    The main entry point of the application.
    """
    groq_api_key = os.environ['GROQ_API_KEY']

    initialize_session_state()

    st.title("Lightning ⚡️")
    st.markdown("Chat with Lightning, an ultra-fast AI chatbot powered by Groq LPUs!")


    model, conversational_memory_length = display_customization_options()

    if st.session_state.model != model:
        # Reset chat history and session state when the model is switched
        st.session_state.chat_history = []
        st.session_state.model = model
        st.experimental_rerun()

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    st.divider()
    if user_question:= st.chat_input("What is up?"):
        st.session_state.chat_history.append({"human": user_question, "AI": ""})
        with st.chat_message("user"):
            st.markdown(user_question)

        for message in st.session_state.chat_history:
            memory.save_context({'input': message['human']}, {'output': message['AI']})

        groq_chat = initialize_groq_chat(groq_api_key, model)
        conversation = initialize_conversation(groq_chat, memory)

        process_user_question(user_question, conversation)

        with st.chat_message("assistant"):
            response = conversation(user_question)
            st.markdown(response['response'])
            st.session_state.chat_history[-1]["AI"] = response['response']

if __name__ == "__main__":
    main()
