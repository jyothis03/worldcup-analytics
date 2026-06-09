import os
import sys
import json
import httpx
from pathlib import Path
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.app.core.config import settings

GITHUB_URL = "https://raw.githubusercontent.com/openfootball/worldcup/master/2026--usa/cup.txt"
response = httpx.get(GITHUB_URL)

if response.status_code != 200:
    print(f"Failed to download file. Status: {response.status_code}")
    sys.exit(1)
cup_content = response.text
print("Successfully downloaded cup.txt!")

class Match(BaseModel):
    id: int = Field(description="A sequential ID for the match, starting from 1")
    date: str = Field(description="Date in ISO 8601 format (e.g., 2026-06-11T13:00:00-06:00). Respect the UTC-X timezone hints.")
    home_team: str = Field(description="The name of the home team")
    away_team: str = Field(description="The name of the away team")
    group: str = Field(description="The group name (e.g., 'Group A')")
    venue: str = Field(description="The name of the stadium/city")

class WorldCupData(BaseModel):
    teams: list[str] = Field(description="A flat list of all 48 unique team names")
    matches: list[Match] = Field(description="The full list of matches extracted from the text")

api_key = settings.gemini_api_key
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Extract the teams and matches from the following World Cup 2026 text file.\n\nTEXT:\n{cup_content}",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=WorldCupData,
            temperature=0.0 # Temperature 0 = factual, no creative guessing
        ),
    )
except Exception as e:
    print(f"Error communicating with Gemini: {e}")
    sys.exit(1)

parsed_data = json.loads(response.text)
data_dir = project_root / "backend" / "data"
data_dir.mkdir(parents=True, exist_ok=True) # Create the data folder if it doesn't exist

with open(data_dir / "fixtures.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data["matches"], f, indent=4)
print(f"Saved {len(parsed_data['matches'])} matches to backend/data/fixtures.json")
with open(data_dir / "teams.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data["teams"], f, indent=4)
print(f"Saved {len(parsed_data['teams'])} teams to backend/data/teams.json")
print(" Phase 1 Data Pipeline complete!")