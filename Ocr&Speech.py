import streamlit as st
import requests
import json
from io import BytesIO
from PIL import Image
import config
from time import sleep


imagclone = BytesIO()


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

    #formatted_text = json.dumps(text, sort_keys=True, indent=4).replace('\\n', '\n')

    #python_obj=json.loads(formatted_text)

    normal = text.replace('\\n', '\n')


    return text

def postapi(text):
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

def getapi(id):

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











imag = st.file_uploader("Choose an image to turn into audio")
if imag is not None and imag != imagclone:
        formatted_text = perform_ocr()
        st.write(formatted_text)
        imagclone=imag
        id ,eta=postapi(formatted_text)
        if id and eta:
            sleep(eta)
            url=getapi(id)
            response = requests.get(url)
            if response.status_code==200:
                st.audio(response.content)
            else:
                st.error("Failed to load the audio")
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