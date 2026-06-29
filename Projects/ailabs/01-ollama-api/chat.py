import requests

URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5-coder:14b"

print("Type 'exit' to quit.\n")

while True:

    prompt = input("You > ")

    if prompt.lower() == "exit":
        break

    response = requests.post(
        URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    print("\nAI >")
    print(response.json()["response"])
    print()