import streamlit as st     
import time
import webbrowser

extract ="http://192.168.100.24:8501"
scrap="http://192.168.100.24:8503"
t2s="http://192.168.100.24:8504"
e2s="http://192.168.100.24:8502"



st.sidebar.image("logo.png", use_column_width=True)

# Add options to sidebar
option = st.sidebar.selectbox(
    'Select an option',
    ('Home','User Guide','GitHub', 'Contact Us', 'Support')
)

footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F5DEB3  ;
        color: #000000;
        text-align: center;
        font-size: 12px;
        padding: 0  px;
    }
    </style>
    <div class="footer">
    <p>Copyright © 2023 - APIverse </p>
    </div>
    """
st.markdown(footer, unsafe_allow_html=True)

# Display selected option
if option == 'Home':
    
    st.header('Welcome to APIverse!')
    st.subheader("Where we're all about APIs, the digital duct tape of the internet! We've got more APIs than you can shake a keyboard at, and we're using them to build all sorts of cool stuff.")
    col1,col2=st.columns([2,3])
    if col1.button('Text Extractor + Summarizer/Translator 👁️‍🗨️📜🌐'):
        time.sleep(1)  
        webbrowser.open(extract)
    if col1.button("Web Scraper + Summarizer 🕸️🕵️‍♂️📝"):
        time.sleep(1)
        webbrowser.open(scrap)
    if col1.button("Translator +/- Text2Speech 🌐📜➡️🔊"):
        time.sleep(1)
        webbrowser.open(t2s)
    if col1.button("Text Extractor + Text2Speech 👁️‍🗨️📜➡️🔊"):
        time.sleep(1)
        webbrowser.open(e2s)
    col2.write("✧ This API can extract a text from an image and either summarizes it or translates it")
    col2.write("")
    col2.write("✧ This API can extract a text from a website and summarizes it ")
    col2.write("")
    col2.write("")
    col2.write("✧ This API can translate a text and turn it into an audio (Text2Speech only supports English)")
    col2.write("")
    col2.write("✧ This API can extract a text from an image and turn it into an audio (Only supports english language)")
elif option == 'GitHub':
    webbrowser.open("https://github.com/Ahmed-YassineElm")
    st.header("Check the opened github tab!")
elif option == 'Contact Us':
    # Add your code for Contact Us page
    st.header("Contact Us page coming soon!")
elif option == 'Support':
    # Add your code for Support page
    st.header("Support page coming soon!")
elif option == 'User Guide':
    st.header("Choose the API you want to watch it's guide!")
    api=st.selectbox(
    'Select an API',
    ('-----','Text Extractor + Summarizer/Translator 👁️‍🗨️📜🌐','Web Scraper + Summarizer 🕸️🕵️‍♂️📝', 'Translator +/- Text2Speech 🌐📜➡️🔊', 'Text Extractor + Text2Speech 👁️‍🗨️📜➡️🔊')
)
    if api == 'Text Extractor + Summarizer/Translator 👁️‍🗨️📜🌐':
        video_file = open('media/OcrTranSumGuide.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif api == 'Web Scraper + Summarizer 🕸️🕵️‍♂️📝':
        video_file = open('media/ScaperSum.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif api == 'Translator +/- Text2Speech 🌐📜➡️🔊':
        video_file = open('media/TransSpeech.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif api == 'Text Extractor + Text2Speech 👁️‍🗨️📜➡️🔊':
        video_file = open('media/OcrSpech.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    

