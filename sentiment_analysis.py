import openai
import streamlit as st 
from pathlib import Path
import configparser

# Initialze the openai key
# Get api key as input from the user 
api_key = st.text_input('Enter Your api key') 
openai.api_key = api_key

def sentiment_analyzer(text):
    """ 
    Function to analyze the sentiment of the given text
    ::params
    text (str): text entered by user
    ::returns
    sentiment (str): sentiment of the tex
    """
    prompt = f"Identify and return the sentiment either positive or negative in given text. text: {text}"
    # Get response from chatgpt
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content':'You are a helpful sentiment analyzer that returns concise sentiment'},
            {'role':'user','content': prompt}
        ],
        temperature=0.1
    )

    sentiment = response.choices[0].message.content
    return sentiment

st.title("Openai Sentiment Analyzer")
text = st.text_input("Enter Text: ", value='I love to learn About AI')

if st.button('submit'):
    with st.spinner('OpenAI processing in Progression'):
        sentiment = sentiment_analyzer(text)
        st.success("OpenAI Processing completed!")
    # Display the sentiment to user 
    st.write(f'Sentiment: {sentiment}')