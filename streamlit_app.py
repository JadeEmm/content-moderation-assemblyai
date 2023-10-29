import streamlit as st
from pytube import YouTube
from utilities import get_yt, transcribe_yt

st.markdown('# **Content Moderation App**')
st.markdown('''
    :gray[Perform content moderation on audio files from YouTube.]''')

st.warning ('Awaiting URL input in the sidebar.')

#Sidebar
st.sidebar.header('Input URL')

#create a form in the sidebar
with st.sidebar.form(key='my_form'):
    URL = st.text_input('Enter the URL of the Youtube video:')
    submit_button = st.form_submit_button(label='Enter')

#Run functions if the URL is entered
if submit_button:
    get_yt(URL)
    transcribe_yt()
    
    with open('transcription.zip', 'rb') as zip_download:
        btn = st.download_button(
            label = ':gray[Download ZIP file]',
            data = zip_download,
            file_name = 'transcription.zip',
            mime = 'application/zip'
        )

with st.sidebar.expander('Example URLs'):
    st.code('https://www.youtube.com/watch?v=fcfQkxwz4Oo') #BBC video
    st.code('https://www.youtube.com/watch?v=A3eHTe2JyW0') #Zoe video:
    st.code('https://www.youtube.com/watch?v=uvqDTbusdUU') #TedX video
    st.code('https://www.youtube.com/watch?v=WcLlpWmEpQ8') #Ted-Ed video
