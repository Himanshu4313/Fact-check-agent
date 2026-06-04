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

    Return ONLY JSON array of strings.

    Text:
    {text[:15000]}
    """

    response = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type":"application/json"
        }
    )
    
    if not response.text:
        print("Empty response received")
        return []
    try:
        return json.loads(response.text)
    except json.JSONDecodeError as e:
        print("JSON Decode Error:",e)
        print("Raw Output:",response.text)
        return []