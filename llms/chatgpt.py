import openai

# Replace 'your-api-key' with your actual OpenAI API key
OPENAI_API_KEY = 'sk-proj-Hrp6h10tqyLfusKMToMQT3BlbkFJt6qKQ3Mg7bSrPezDKzC4'

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPENAI_API_KEY,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)