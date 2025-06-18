# Voite Bot

A Streamlit-based voice interview bot that answers questions as if it were you, Sagar Kumar, using your background, experience, and skills. The app uses OpenAI's GPT-4o-mini model for natural, first-person answers, and can accept both voice and text input.

## Features
- **Personalized Q&A:** Answers every question as Sagar, based on your real background, projects, and achievements.
- **Voice & Text Input:** Ask questions by speaking or typing.
- **Text-to-Speech:** Bot replies with both text and voice.
- **Modern UI:** Clean, readable interface with sidebar instructions and sample questions.
- **Error Handling:** Friendly messages for speech recognition or API errors.

## Technologies Used
- [Streamlit](https://streamlit.io/) for the web UI
- [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models/gpt-4o) for generating answers
- [pyttsx3](https://pyttsx3.readthedocs.io/) for text-to-speech
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) for voice input

## Setup & Usage
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Set your OpenAI API key:**
   The API key is currently hardcoded in `app.py`. Replace it with your own if needed.
3. **Run the app:**
   ```bash
   streamlit run app.py
   ```
4. **Open in your browser:**
   Visit [http://localhost:8501](http://localhost:8501)

## Customization
- To change the persona, edit the `system` message in the `get_response` function in `app.py`.
- To use a different OpenAI model or API key, update the `client` initialization in `app.py`.


