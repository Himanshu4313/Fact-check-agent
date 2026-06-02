import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def verify_claim(claim, evidence):

    prompt = f"""
    Claim:
    {claim}

    Evidence:
    {evidence}

    Decide:

    VERIFIED
    INACCURATE
    FALSE

    Return JSON:
    {{
      "status":"",
      "reason":"",
      "correct_fact":""
    }}
    """

    response = model.generate_content(prompt)

    return response.text