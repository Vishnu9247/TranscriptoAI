import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import google.generativeai as genai
import os
#from dotenv import load_dotenv

#load_dotenv()

GEMINI_API_KEY = os.getenv("GEN_AI_API_KEY")
if not GEMINI_API_KEY:
    st.text(GEMINI_API_KEY)
    st.error("API key is missing or invalid.")
    st.stop()
    
genai.configure(api_key = GEMINI_API_KEY)
genai_model = genai.GenerativeModel('models/gemini-1.5-flash')


def clean_and_format_text(input_text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", input_text)
    text = re.sub(r"^\s*\*\s*", "- ", text, flags=re.MULTILINE)
    text = re.sub(r"\n\s*\*\s*", "\n  - ", text)  
    text = re.sub(r"^(\s*)([IVXLCDM]+\..*?)$", r"\1### \2", text, flags=re.MULTILINE)
    text = re.sub(r"(\n\s*){2,}", "\n\n", text)
    return text


header = st.container()
body = st.container()
foot = st.container()

with header:
    st.title("TranscriptoAI")
    st.text("Please paste the youtube link you want to summarize and click enter, we will provide you with the summary")

i = 0
with body:
    link = st.text_input("please, paste your youtube link here")
    if (len(link) >1):
        pattern = r"(?<=v=)[\w-]+"
        match = re.search(pattern, link)
        if match:
            video_id = match.group()
        else:
            st.text("Please provide a valid link")
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        transcript = TextFormatter().format_transcript(transcript)

    
        options = ["Summarize", "Make Notes", "Custom prompt"]
        selected_option = st.selectbox("Choose from the dropdown:", options)

        if selected_option == "Custom prompt":
            prompt = st.text_input("please enter your custom prompt")
        else:
            prompt = selected_option

        response = genai_model.generate_content(prompt + transcript, stream = False)
        st.subheader("The requested content is as shown below:")
        summary = response.text
        summary = clean_and_format_text(summary)
        i = 1
        

    else:
        st.text("please enter a valid link")
    
    
with foot:
    if i == 1:
        st.text(summary)
    else:
        pass
