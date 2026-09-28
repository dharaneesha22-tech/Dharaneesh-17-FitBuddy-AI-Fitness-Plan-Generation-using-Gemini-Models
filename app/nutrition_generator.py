
import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


if not API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Add your Gemini API key to the .env file."
    )


client = genai.Client(api_key=API_KEY)


def generate_nutrition_tip(
    goal: str,
    weight: float
) -> str:

    prompt = f"""
You are FitBuddy, an AI fitness assistant.

Give a simple nutrition and recovery guide.

User details:
Fitness Goal: {goal}
Weight: {weight} kg

Requirements:
1. Give practical nutrition suggestions.
2. Suggest suitable protein and healthy food choices.
3. Give hydration advice.
4. Give basic recovery and sleep advice.
5. Keep the answer simple and easy to follow.
6. Do not provide extreme diets or unsafe medical advice.
7. Add a short disclaimer to consult a qualified professional for medical or dietary conditions.

Return only the nutrition and recovery guide.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response.text:
            return response.text

        return "Unable to generate nutrition advice."

    except Exception as e:

        return f"Gemini error: {str(e)}"
