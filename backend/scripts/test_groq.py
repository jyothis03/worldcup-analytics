import os
import sys
sys.path.append(".")
import json
from groq import Groq
from backend.app.models.prediction import PredictionResponse

# Load keys
from dotenv import load_dotenv
load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

schema_blueprint = PredictionResponse.model_json_schema()

system_prompt = f"""
You are an elite football tactical analyst generating a highly structured prediction in valid JSON format.

MATCH:
Mexico vs South Africa
Group: A
Date: 2026-06-12

VENUE:
Stadium: Azteca
Altitude: 2200m above sea level
Climate: Hot

Mexico:
FIFA Rank: 12
Base camp: Mexico City

South Africa:
FIFA Rank: 45
Base camp: Guadalajara

LIVE WEB RESEARCH (Injuries, Form, XI, H2H):
- Mexico: Lozano is doubtful.
- South Africa: Percy Tau is starting.

ANALYSIS INSTRUCTIONS:
- Venue impact: evaluate altitude difference.

You MUST output your response in valid JSON format matching this exact schema:
{json.dumps(schema_blueprint, indent=2)}
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Generate the tactical prediction in JSON based on the static and live data."}
]

response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=0.2,
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)
