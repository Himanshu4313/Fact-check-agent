import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_claims(text):

    prompt = f"""
    Extract factual claims from the text.

    Focus on:
    - statistics
    - percentages
    - dates
    - revenue
    - financial figures
    - technical facts

    Return ONLY JSON array.

    Text:
    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return json.loads(response.text)