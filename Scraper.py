import requests
import streamlit as st
from bs4 import BeautifulSoup
import config

def send_request(url):
    response = requests.get(
        url,
        params={
            'api_key': config.scrapingbee_key,
            'url': 'https://www.sap.com/products/erp/what-is-erp.html',  
        },
        
    )
    #print('Response HTTP Status Code: ', response.status_code)
    #st.write('Response HTTP Response Body: ', response.content)
    my_string = response.content.decode('utf-8')
    soup = BeautifulSoup(my_string, "html.parser")
    text=soup.get_text()
    return text
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

url=''
formatted_text=''
numsenttest=0
st.header("Scraping and Summarizing")
url=st.text_input("Enter the site you want to scrap and summarize")
if url != '':
    formatted_text=send_request(url)
    num_sentences = st.number_input('Enter the minimum number of sentences')
    if num_sentences is not None and num_sentences != numsenttest and formatted_text !='':
        if num_sentences<3:
                num_sentences=3
        numsenttest = num_sentences
        text=summarize_text(formatted_text,int(num_sentences))
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

