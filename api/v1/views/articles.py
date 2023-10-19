"""This module implements the GPT-4 API"""
import os
import openai
from dotenv import load_dotenv
# from api.v1.views import auth
# from models import article
# from models import autosave
# from models import user

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": \
            "Your task is to generate an article on the following topic: {Topic/Keywords}. \
            The article should be informative, engaging, and approximately \
                {Word count} words long. \
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
