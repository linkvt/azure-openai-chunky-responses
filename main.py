import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = "2023-05-15"

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


def create_chat_response(prompt: str):
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        stream=True,
    )

    for chunk in response:
        chunk_message = chunk["choices"][0]["delta"]  # extract the message

        print_text = ""
        if "content" in chunk_message:
            print_text = chunk_message["content"]

        print(print_text, end="")


print("####")
print("Example of chunky responses, API always responds chunk on a line break")
print("####")
create_chat_response(
    "Write me a 200 word article on compliance for private companies in Wyoming."
)

print("\n\n####")
print(
    "Example with a single large paragraph, which delays the response even further (as no response on linebreak possible)"
)
print("####")

create_chat_response(
    "Write me a 200 word article on compliance for private companies in Wyoming in a single large paragraph."
)
