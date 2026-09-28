
import os

from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


# Create Gemini client
if not API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is missing. "
        "Add your Gemini API key to the .env file."
    )

client = genai.Client(api_key=API_KEY)


def generate_workout(
    name: str,
    age: int,
    weight: float,
    goal: str,
    intensity: str
) -> str:

    prompt = f"""
You are FitBuddy, an AI fitness assistant.

Create a safe and beginner-friendly 7-day workout plan.

User details:
Name: {name}
Age: {age}
Weight: {weight} kg
Fitness Goal: {goal}
Workout Intensity: {intensity}

Requirements:
1. Create a 7-day workout plan.
2. Clearly mention Day 1 to Day 7.
3. Include exercises and approximate duration.
4. Include rest or recovery where appropriate.
5. Keep the plan practical and easy to follow.
6. Do not provide dangerous or extreme exercises.
7. Add a short safety note at the end.

Return only the workout plan.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if response.text:
            return response.text

        return "Unable to generate workout plan."

    except Exception as e:

        return f"Gemini error: {str(e)}"

