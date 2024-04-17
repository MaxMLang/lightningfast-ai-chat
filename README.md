# Lightning Chatbot

<p align="center">
  <img src="assets/logo.png" alt="Lightning Chatbot Logo" width="200" height="200">
</p>

[![GitHub Stars](https://img.shields.io/github/stars/MaxMLang/lightningfast-ai-chat?style=social)](https://github.com/yourusername/lightning-chatbot/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/MaxMLang/lightningfast-ai-chat)](https://github.com/yourusername/lightning-chatbot/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/MaxMLang/lightningfast-ai-chat)](https://github.com/yourusername/lightning-chatbot/pulls)
[![License](https://img.shields.io/github/license/MaxMLang/lightningfast-ai-chat)](https://github.com/yourusername/lightning-chatbot/blob/main/LICENSE)

Lightning is an ultra-fast AI chatbot powered by Groq LPUs (Language Processing Units), offering one of the fastest inference speeds on the market as of April 2024. With its advanced natural language processing capabilities and lightning-fast response times, Lightning provides an unparalleled conversational experience.

## [Click here to try it out](https://lightning-ai.streamlit.app/)

## Features

- ⚡ Ultra-fast inference powered by Groq LPUs
- 🎨 Customizable model selection and conversational memory length
- 💬 Seamless conversation history tracking
- 🌐 Easy deployment using Streamlit web framework

## Installation

1. Clone the repository:git clone https://github.com/MaxMLang/lightningfast-ai-chat.git
2. Navigate to the project directory: 
  ```
cd lightningfast-ai-chat
  ```
3. Install the required dependencies: 
```
pip install -r requirements.txt
  ```
4. Set up the Groq API key:

- Create a `.env` file in the project directory.
- Add the following line to the `.env` file, replacing `your_api_key` with your actual Groq API key:

  ```
  GROQ_API_KEY=your_api_key
  ```

5. Run the chatbot:
  ```
streamlit run app.py
  ```

6. Open the provided URL in your web browser to access the Lightning Chatbot interface.

## Usage

1. Choose a language model from the sidebar.
2. Adjust the conversational memory length using the slider in the sidebar.
3. Type your question or message in the input field and press Enter.
4. Lightning will generate a response using the selected model and display it in the chat interface.
5. Continue the conversation by entering more questions or messages.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Groq](https://groq.com) for providing the lightning-fast LPUs.
- [Langchain](https://github.com/hwchase17/langchain) for the powerful language modeling capabilities.
- [Streamlit](https://streamlit.io) for the intuitive web framework.


