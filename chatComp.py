import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim."}
    ]
)

print(response.choices[0].message['content'].strip())
