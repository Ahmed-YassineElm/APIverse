import requests
import streamlit as st
import config
import json
from googletrans  import Translator
from time import sleep




def translate(formatted_text,selected_lang):
    translator = Translator()
    output=translator.translate(formatted_text, dest=selected_lang)
    return output.text

def post(text):
    url = "https://large-text-to-speech.p.rapidapi.com/tts"

    payload = { "text": text}
    headers = {
    	"content-type": "application/json",
	    "X-RapidAPI-Key": config.postget_key,
    	"X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    resp=response.json()
    return resp['id'],resp['eta']

def get(id):

    url = "https://large-text-to-speech.p.rapidapi.com/tts"

    querystring = {"id":id}

    headers = {
	    "X-RapidAPI-Key": config.postget_key,
	    "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    resp=response.json()
    output=resp['url']
    return output
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





formatted_text=st.text_input("Write the text you want translated")
languages=languages = ['-----','af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
selected_lang=st.selectbox("Select the language you want to translate to",languages)
if formatted_text and selected_lang != '-----':
    out=translate(formatted_text,selected_lang)
    st.write(out)
    if selected_lang == 'en':
        choice = st.checkbox("Do you want to transform the text to speech ?")
        if choice :
            id,eta=post(out)
            if id and eta:
                sleep(eta)
                url=get(id)
                response = requests.get(url)
                if response.status_code==200:
                    st.audio(response.content)
                else:
                    st.error("Failed to load the audio")
