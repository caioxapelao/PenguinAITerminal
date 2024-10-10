from openai import OpenAI

client = OpenAI(
    api_key="dont remove this",
    base_url="https://proxy.mubilop.tech/v1",
)
model = input("Choose a model: ")
sysprompt = input("System Prompt: ")

while True:
    prompt = input("Enter Prompt: ")

    chat_completion = client.chat.completions.create(
        messages=[
         {
            "role": "system",
            "content": sysprompt
         },
         {
             "role": "user",
             "content": prompt,
         }
     ],
        model=model,
    )

    response = chat_completion.choices[0].message.content
    print(response)
