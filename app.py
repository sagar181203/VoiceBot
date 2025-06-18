import streamlit as st
from openai import OpenAI
import pyttsx3

# Streamlit page config
st.set_page_config(page_title="Voite Bot", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f7f9fa; }
    .stButton>button {
        background: linear-gradient(90deg, #5A9FFF 0%, #6EE7B7 100%);
        color: white; border-radius: 8px; font-weight: bold; padding: 0.5em 2em; margin-top: 1em;
    }
    .response-box {
        background: #f8fafc; border-radius: 10px; padding: 1.5em; margin-top: 1em;
        box-shadow: 0 2px 8px rgba(90,159,255,0.08); font-size: 1.15em; color: #1a202c;
        font-weight: 600; border: 1.5px solid #5A9FFF;
    }
    .question-box {
        background: #e6f7ff; border-radius: 10px; padding: 0.8em; margin-top: 0.5em;
        font-size: 1.08em; color: #1a202c; font-weight: 700; border: 1.5px solid #5A9FFF;
    }
    .info-visible {
        background: #e3f8ff !important; color: #1a2b3c !important; font-weight: 700 !important;
        padding: 0.7em 1.2em !important; border-radius: 8px !important; margin-bottom: 0.5em !important;
        border: 1.5px solid #5A9FFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.image("https://img.icons8.com/color/96/000000/robot-2.png", width=72)
st.sidebar.title("Voice Bot")
st.sidebar.markdown("""
**How to use:**
- Choose to speak or type your question.
- Get instant answers with voice!
- Powered by ChatGPT (OpenAI) for all questions.

**Sample Questions:**
  - What should we know about your life story?
  - What's your number one superpower?
  - What are the top three areas you'd like to grow in?
  - What misconception do your coworkers have about you?
  - How do you push your boundaries and limits?
""")

# OpenAI client from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Response generation function
def get_response(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": (
                    "You are Sagar Kumar, a real person. "
                    "You are originally from India, belong to Bihar, and currently based in Karnataka for your education and work. "
                    "You have a Bachelor's degree in Artificial Intelligence and Machine Learning from PES Institute of Technology and Management, with an aggregate CGPA or GPA of 9.14/10. "
                    "You are highly passionate about AI & ML, with hands-on experience in Deep Learning, NLP, Computer Vision, and GenAI technologies. "
                    "You have completed multiple internships, including a Deep Learning Internship at ResoluteAI Software Pvt Ltd, Infosys Springboard Internship 5.0, and Dhee Coding Lab. "
                    "You have worked on projects such as language translation with voice cloning, speech-to-text, emotion detection, face recognition attendance, lip-syncing, and EV fleet monitoring. "
                    "You have strong technical skills in Python, TensorFlow, PyTorch, Hugging Face, AWS Bedrock, GANs, LangChain, and more. "
                    "You always answer questions from your own personal perspective based on your knowledge and experience. "
                    "Always reply as yourself, in the first person, naturally and authentically."
                )},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I couldn't get an answer. Error: {str(e)}"

# Text-to-speech
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Text-to-Speech error: {e}")

# Main app
def main():
    st.markdown("<h1 style='text-align:center;color:#5A9FFF;'>🎙️ Voite Bot</h1>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center; color:#6EE7B7; font-size:1.2em;'>Ask me interview questions and I'll reply with voice and text!</div>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns([1, 1])
    with col1:
        option = st.radio("Choose input method:", ["🎤 Speak", "⌨️ Type"], index=0)

    user_question, response, error = None, None, None

    if option == "🎤 Speak":
        audio_file = st.audio_input("🎤 Record your question")
        if audio_file is not None:
            st.audio(audio_file, format="audio/wav")
            with st.spinner("Transcribing..."):
                try:
                    transcript = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        response_format="text"
                    )
                    st.markdown(f'<div class="question-box">You asked: <b>{transcript}</b></div>', unsafe_allow_html=True)
                    response = get_response(transcript)
                except Exception as e:
                    error = f"Audio transcription failed: {str(e)}"

    elif option == "⌨️ Type":
        user_question = st.text_input("Type your question here:")
        if st.button("💬 Ask") and user_question:
            st.markdown(f'<div class="question-box">You asked: <b>{user_question}</b></div>', unsafe_allow_html=True)
            response = get_response(user_question)

    if error:
        st.markdown(f'<div class="response-box" style="color:#b91c1c;background:#ffeaea;border:1.5px solid #ff6a6a;">{error}</div>', unsafe_allow_html=True)
    if response:
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)
        speak(response)

if __name__ == "__main__":
    main()
