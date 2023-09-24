import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "user", 
         "content": "Hello world"}
    ])

print(response['choices'][0]['message']['content'])
