import requests
url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen2.5-coder:14b",
    "prompt": "Say hello in one sentence.",
    "stream": False
}
response = requests.post(url, json = payload)
print(response.json()["response"])
