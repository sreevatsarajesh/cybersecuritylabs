import requests

from config import URL, MODEL, STREAM, TIMEOUT


def generate(prompt: str):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": STREAM
    }

    response = requests.post(
        URL,
        json=payload,
        timeout=TIMEOUT
    )

    response.raise_for_status()

    return response.json()["response"]