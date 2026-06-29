import json
import requests

from config import URL, MODEL, TIMEOUT

prompt = input("Prompt > ")

response = requests.post(
    URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": True
    },
    stream=True,
    timeout=TIMEOUT
)

print()

for line in response.iter_lines():

    if line:

        data = json.loads(line)

        print(data.get("response", ""), end="", flush=True)

print()