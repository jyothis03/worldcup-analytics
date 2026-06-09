import os
import sys
import json
from pathlib import Path
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# Setup paths
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from backend.app.core.config import settings

print("Starting Phase 1.5: Enriching Venues and Teams...")

data_dir = project_root / "backend" / "data"

# 1. Load the data we generated in Phase 1
with open(data_dir / "fixtures.json", "r", encoding="utf-8") as f:
    fixtures = json.load(f)

with open(data_dir / "teams.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

# 2. Extract just the unique venue names so we don't send duplicates to Gemini
unique_venues = list(set([match["venue"] for match in fixtures]))

print(f"Loaded {len(teams)} teams and {len(unique_venues)} unique venues.")

# 3. Define the exact JSON schema we want Gemini to output
class Venue(BaseModel):
    name: str = Field(description="The name of the stadium/city as provided")
    altitude_meters: int = Field(description="The altitude of the stadium in meters above sea level")
    summer_climate: str = Field(description="A short 1-3 word description of the expected June/July climate (e.g., 'Hot and Humid', 'Mild', 'Dry Heat')")

class TeamStat(BaseModel):
    team_name: str = Field(description="The name of the country as provided")
    fifa_ranking: int = Field(description="The team's current FIFA World Ranking (1 to 200+) make sure to get it accurate from FIFA.")
    base_camp_location: str = Field(description="The official North American host region for this team's World Cup training base camp.")

class EnrichedData(BaseModel):
    venues: list[Venue] = Field(description="The enriched data for all provided venues")
    team_stats: list[TeamStat] = Field(description="The enriched stats for all provided teams")

# 4. Call Gemini to enrich the data
api_key = settings.gemini_api_key
if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

print("Asking Gemini for Altitude, Climate, and FIFA Rankings... (this may take 20-30 seconds)")

prompt = f"""
You are a football data analyst preparing data for the 2026 World Cup.
Please provide the factual altitude and expected summer climate for the following venues:
{json.dumps(unique_venues)}

And provide the current FIFA ranking and expected/official Base Camp location for these teams:
{json.dumps(teams)}
"""

try:
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=EnrichedData,
            temperature=0.0 # Factual answers only
        ),
    )
except Exception as e:
    print(f"Error communicating with Gemini: {e}")
    sys.exit(1)

# 5. Save the output
parsed_data = json.loads(response.text)

with open(data_dir / "venues.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False keeps special characters human-readable!
    json.dump(parsed_data["venues"], f, indent=4, ensure_ascii=False)
print(f"Saved {len(parsed_data['venues'])} venues to backend/data/venues.json")

with open(data_dir / "team_stats.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data["team_stats"], f, indent=4, ensure_ascii=False)
print(f"Saved {len(parsed_data['team_stats'])} team stats to backend/data/team_stats.json")

print("Phase 1.5 Data Enrichment complete!")
