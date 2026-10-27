from openai import OpenAI

client = OpenAI()  # Reads OPENAI_API_KEY from the environment.

response = client.responses.create(
    model='gpt-4.1-mini',
    input="how to store api key in python project and how to access it through code?"
)

print(response)