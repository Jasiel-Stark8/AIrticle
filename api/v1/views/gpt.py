"""This module implements the GPT-4 API"""
import os
import openai
from dotenv import load_dotenv
from flask import request
# from api.v1.views import auth
# from models import article
# from models import autosave
# from models import user

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get article parameters from client to feed to GPT
topic = request.form['topic']
keywords = request.form['keywords'].split(' ')
word_count = request.form['word_count']
article_length = {
    'short': 400,
    'medium': 1000,
    'long': 2500
}

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": \
            "Your task is to generate an article on the following topic and keywords: {topic/keywords}. \
            The article should be informative, engaging, and approximately \
                {Word_count} words long. \
                Please include an introduction, main body, and conclusion."},
        {"role": "user", "content": "{animals}{sahara south africa}"},
    ],
    temperature=0.7,
    stream=True
)

try:
    for chunk in response:
        print(chunk)
except Exception:
    print('There was an error generating your article \
        Kindly click the generate button again to generate')
