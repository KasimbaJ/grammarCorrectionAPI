import os
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("Enter a phrase to correct to standard English: ")
user_input = str(input())
print(user_input)

response = openai.Completion.create(
  engine="text-davinci-001",
  prompt=user_input,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0

)
print(response)
keywords_text: str = response["choices"][0]["text"]
print(keywords_text)