import streamlit as st
import base64
from seleniumnyu import cv_test

# Initialize session state variables if they don't exist
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

# Page configuration
st.set_page_config(page_title="Konect U",
                   page_icon="https://raw.githubusercontent.com/juicjaane/blueai/main/logo_2.jpg",
                   layout="wide")

# Custom CSS to improve the look and feel and position the input at the bottom
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    .stApp {
        max-width: 800px;
        margin: 0 auto;
        font-family: 'Roboto', sans-serif;
        background-color: #ffffff; /* White Background */
        color: #000000; /* Black Text */
    }
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        padding: 20px;
    }
    .title-text {
        font-size: 48px;
        font-weight: 700;
        margin: 0;
        background: linear-gradient(45deg, #FFD700, #FF4500); /* Golden to Red Gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for readability */
    }
    .stTextInput > div > div > input {
        background-color: #f0f0f0; /* Light Gray Background for Text Box */
        border: 1px solid #cccccc; /* Light Gray Border */
        color: #000000; /* Black Text */
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton > button {
        width: 100%;
        background-color: #1f2937; /* Dark Gray for Button */
        color: #ffffff; /* White Text */
        border: none;
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #161921; /* Darker Gray on Hover */
    }
    .user-container {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 10px;
    }
    .bot-container {
        display: flex;
        justify-content: flex-start;
        margin-bottom: 10px;
    }
    .user-message, .bot-message {
        padding: 10px;
        border-radius: 10px;
        color: #000000; /* Black Text */
        max-width: 60%;
    }
    .user-message {
        background-color: #e0e0e0; /* Light Gray for User Messages */
        margin-left: auto; /* Pushes user message to the right */
        text-align: right;
    }
    .bot-message {
        background-color: #d0d0d0; /* Slightly Darker Gray for Bot Messages */
        margin-right: auto; /* Pushes bot message to the left */
        text-align: left;
    }
    .chat-input-container {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #ffffff; /* White Background for Input Container */
        padding: 10px 0;
        box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1); /* Lighter Shadow for Input Container */
    }
    .stTextInput {
        max-width: 800px;
        margin: 0 auto;
    }
</style>

""", unsafe_allow_html=True)
# Display title with logo
st.markdown("""
    <div class="title-container">
        <img src="https://raw.githubusercontent.com/juicjaane/blueai/main/logo_2.jpg" style="width: 80px; margin-right: 20px;">
        <h1 class="title-text">Konect U</h1>
    </div>
""", unsafe_allow_html=True)


#def clear_input():

# User input
def get_text():
    return st.text_input("You:", key="input")


def play_audio(file_path: str):
    # Read the audio file and encode it in base64
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()  # Convert to base64 and decode to string

    # Create the HTML with the base64-encoded audio and autoplay, with hidden controls
    audio_html = f"""
    <audio autoplay="true" style="display: none;">
        <type="audio/mp3">
    </audio>
    <script>
        var audio = document.createElement('audio');
        audio.src = "data:audio/mp3;base64,{b64}";
        audio.autoplay = true;
        audio.style.display = "none";
        document.body.appendChild(audio);
    </script>
    """

    # Inject the HTML into Streamlit
    st.components.v1.html(audio_html, height=0)


def generate_response(prompt):
    response_text = ""
    audio_file = ""
    prompt_lower = prompt.lower()

    if prompt_lower == "hello":
        response_text = "Hello Kevin, How can I assist you today? Are we working on an application form?"
        audio_file = "hellokevin.mp3"
    elif prompt_lower == "yes":
        response_text = "Awesome! Have you already updated your profile and uploaded the SOP and resume you received from Nalanda?"
        audio_file = "Awesome.mp3"
    elif prompt_lower == "yes, everything is done":
        response_text = "Perfect! I'll start filling out the application form now."
        audio_file = "perfect.mp3"
    elif "sure, fill my form" in prompt_lower:
        try:
            cv_test()
            response_text = "Form filling completed. Thank you. I will let you know about your form status soon."
            audio_file = "formcomplete.mp3"
        except Exception as e:
            response_text = f"Error: Failed to fill the form. {str(e)}"
            audio_file = "error.mp3"  # Add an audio file for error cases
    else:
        response_text = "Sorry, I didn't understand that. Can you please rephrase or ask something else?"
        audio_file = "default.mp3"  # Add a default audio file for unrecognized inputs

    return response_text, audio_file


# Main chat interface
user_input = get_text()

if user_input:
    response_text, audio_file = generate_response(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(response_text)

    if audio_file:
        play_audio(audio_file)

# Display the conversation
for i in range(len(st.session_state['generated'])):
    # User message container (right-aligned)
    st.markdown(
        f"<div class='user-container'><div class='user-message'><strong>You:</strong> {st.session_state['past'][i]}</div></div>",
        unsafe_allow_html=True
    )
    # Bot message container (left-aligned)
    st.markdown(
        f"<div class='bot-container'><div class='bot-message'><strong>KonectU:</strong> {st.session_state['generated'][i]}</div></div>",
        unsafe_allow_html=True
    )