"""This module implements the GPT-4 API"""
import os
import openai
from dotenv import load_dotenv
# from models import article
# from models import user

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_article(topic, keywords, article_length):
    """GPT validation and generation"""
    # Determine word count based on article_length
    word_count = {
        'short': '500',
        'medium': '1000',
        'long': '2000'
    }.get(article_length, '1000')  # Default to medium if not recognized

    if not word_count:
        article_length = word_count.keys(1)

    # Adjust the content strings with the provided values
    system_message = f"Your task is to generate an article on the topic: {topic}. Keywords: {keywords}. \
                      The article should be informative, engaging, and approximately {word_count} words long. \
                      Please include an introduction, main body, and conclusion."
    user_message = f"{topic} {keywords}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        stream=True
    )

    # Capture the response
    generated_content = []
    try:
        for chunk in response:
            generated_content.append(chunk['choices'][0]['message']['content'])
        return ' '.join(generated_content)
    except Exception as e:
        return f'There was an error generating your article: {e}. \
            Kindly click the generate button again.'
