import streamlit as st
import requests
import json
from io import BytesIO
from PIL import Image
import config
import detectlanguage

detectlanguage.configuration.api_key = "f8ed407ee7328d7b06ef4c0513f25df3"



imagclone = BytesIO()
numsenttest=0

def perform_ocr():
    global imag
    image = Image.open(imag)
    img_bytes = BytesIO()
    image.save(img_bytes, format='JPEG')
    img_bytes.seek(0)
    

    url = "https://ocr-extract-text.p.rapidapi.com/ocr"


    headers = {
	    "X-RapidAPI-Key": config.ocr_key,
	    "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
    }

    response = requests.post(url, files={"image": img_bytes}, headers=headers)
    response.raise_for_status()

    #print(response.json())
    text=response.json()['text']

    formatted_text = json.dumps(text, sort_keys=True, indent=4).replace('\\n', '\n')

    return formatted_text


def summarize_text(formatted_text,num_sentences):
    url = "https://gpt-summarization.p.rapidapi.com/summarize"
    payload = dict(text=formatted_text,num_sentences=num_sentences )
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": config.summarize_key,
    "X-RapidAPI-Host": "gpt-summarization.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    text=response.json()
    output=text["summary"]
    return output   


def translate_text(formatted_text,fromlanguage,language_selected):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
	    "q": formatted_text,
	    "target": language_selected,
	    "source": fromlanguage
    }
    headers = {
	    "content-type": "application/x-www-form-urlencoded",
    	"Accept-Encoding": "application/gzip",
	    "X-RapidAPI-Key": config.translategoogle_key,
	    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    response=response.json()
    output=response['data']['translations'][0]['translatedText']
    return output








imag = st.file_uploader("Choose a file")
options = ['--------', 'Summarize', 'Translate']
selected_option = st.selectbox('Select an option', options)
if selected_option == "Summarize":
    if imag is not None and imag != imagclone:
            formatted_text = perform_ocr()
            st.write(formatted_text)
            imagclone=imag
    num_sentences = st.number_input('Enter the minimum number of sentences')
    if num_sentences is not None and num_sentences != numsenttest:
        if num_sentences<3:
                num_sentences=3
        numsenttest = num_sentences
        text=summarize_text(formatted_text,int(num_sentences))
        st.write(text)
elif selected_option == "Translate":
    if imag is not None and imag != imagclone:
        formatted_text = perform_ocr()
        imagclone=imag
    languages=['-----','am', 'ar', 'be', 'be', 'bi', 'bj', 'bn', 'bo', 'br', 'bs', 'ca', 'co', 'cs', 'cy', 'da', 'dz', 'de', 'dv', 'el', 'en', 'es', 'et', 'eu', 'fa', 'fi', 'fn', 'fo', 'fr', 'gl', 'gu', 'ha', 'he', 'hi', 'hr', 'hu', 'id', 'is', 'it', 'ja', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lo', 'lv', 'me', 'mg', 'mi', 'ms', 'mt', 'my', 'ne', 'ni', 'nl', 'no', 'ny', 'ur', 'pa', 'pa', 'ps', 'pi', 'pl', 'pt', 'rn', 'ro', 'ru', 'sg', 'si', 'sk', 'sm', 'sn', 'so', 'sq', 'sr', 'sv', 'sw', 'ta', 'te', 'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'uk', 'uz', 'vi', 'wo', 'xh', 'yi', 'zu']
    language_selected=st.selectbox("Select a language",languages)
    if language_selected !=  '-----':
        fromlanguage=detectlanguage.simple_detect(formatted_text)
        text=translate_text(formatted_text,fromlanguage,language_selected)
        st.write(text)
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
        
          
    



