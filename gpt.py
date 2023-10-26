import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": ""},
        ],
        temperature=0.7,
        stream=True
    )

# Capture the response
generated_content = []
try:
    for chunk in response:
        print(chunk)
        if 'choices' in chunk and 'delta' in chunk['choices'][0]:
            generated_content.append(chunk['choices'][0]['delta']['content'])
    print(' '.join(generated_content))
except Exception as e:
    print(f'Error: {e}')
