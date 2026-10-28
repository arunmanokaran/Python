from groq import Groq

client = Groq()  # Reads GROQ_API_KEY from the environment.  # Reads OPENAI_API_KEY from the environment.

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": """Write me an email that I need to send it to my team lead asking leave for 3 days because of health issues.

            Make sure that the email is more professional.
            """,
        }
    ],
)

# response = client.responses.create(
#     model='gpt-4.1-mini',
#     input="how to store api key in python project and how to access it through code?"
# )

print(response.choices[0].message.content)
