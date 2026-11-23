# Model

import os
from google import genai

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=gemini_api_key)


def gemini(prompt: str) -> str:
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
    )
    return interaction.output_text