import requests
import os

class AvalAILLM:
    def __init__(self):
        self.api_key = os.getenv("AVALAI_API_KEY")
        self.base_url = os.getenv("AVALAI_BASE_URL")

    def chat(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-4.1-mini",
            "messages": [
                {"role": "system", "content": "شما یک دستیار هوشمند سفر هستید."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=payload
        )

        return response.json()["choices"][0]["message"]["content"]
