import json
import requests

URL = "http://localhost:11434/api/generate"

prompt = input("Prompt > ")

response = requests.post(
    URL,
    json={
        "model": "qwen2.5-coder:14b",
        "prompt": prompt,
        "stream": True
    },
    stream=True
)

print()

for line in response.iter_lines():

    if line:

        data = json.loads(line)

        print(data.get("response", ""), end="", flush=True)

print()