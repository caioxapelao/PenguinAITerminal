from openai import OpenAI

client = OpenAI(
    api_key="dont remove this",
    base_url="https://proxy.mubilop.tech/v1",
)
model = input("Choose a model: ")
sysprompt = input("System Prompt: ")
history = [
    {"role": "system", "content": sysprompt}
]
while True:
    prompt = input("Enter Prompt: ")
    history.append({"role": "user", "content": prompt})

    chat_completion = client.chat.completions.create(
        messages=history,
        model=model,
    )

    response = chat_completion.choices[0].message.content
    print(response)
    history.append({"role": "assistant", "content": response})
