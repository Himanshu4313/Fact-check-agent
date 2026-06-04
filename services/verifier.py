import google.generativeai as genai
import os
import json
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def verify_claim(claims):

    prompt = f"""
    You are a professional fact checker.

    For each claim, analyze the evidence and return:

    - status
    - reason
    - correct_fact

    Return ONLY valid JSON.

   Example:

   [
     {{
       "claim":"Google was founded in 1998",
       "status":"TRUE",
       "reason":"Evidence confirms the founding year.",
       "correct_fact":""
     }}
   ]

    Data:
    {json.dumps(claims,indent=2)}
    """

    response = model.generate_content(
        prompt,
        generation_config={
            "response_mime_type":"application/json"
        }
        )

    return json.loads(response.text)