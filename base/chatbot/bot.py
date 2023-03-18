import os
import openai


class ChatBot:
    def __init__(self, model, api_key, max_tokens=50, temperature=0.9):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        openai.api_key = api_key

    def chat(self, user_input):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{user_input}"},
            ],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return response["choices"][0]["message"]
