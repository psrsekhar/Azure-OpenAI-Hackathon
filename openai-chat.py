import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

client = AzureOpenAI(
    azure_endpoint=os.getenv("ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "system", "content": "You are a helpful, fun and friendly sales assistant for CGE Works, a bicycle and bicycle accessories store."},
    {"role": "user", "content": "Do you sell bicycles?"},
    {"role": "assistant", "content": "Yes, we do sell bicycles. What kind of bicycle are you looking for?"},
    {"role": "user", "content": "I'm not sure what I'm looking for. Could you help me decide?"}
]

response = client.chat.completions.create(
    model = MODEL_NAME,
    messages = MESSAGES,
)

print(response.choices[0].message.content)