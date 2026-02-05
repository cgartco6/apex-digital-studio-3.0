import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class LLMRouter:
    def __init__(self, provider="openai"):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        if self.provider == "openai":
            return self._openai(prompt)
        return "Local LLM response placeholder"

    def _openai(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
