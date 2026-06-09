from google import genai
from google.genai import types
import json, time
from backend.app.core.config import settings
from backend.app.services.data_service import get_match_by_id, get_all_teams, get_all_venues
from backend.app.models.prediction import PredictionResponse



def build_match_context(match_id: int):

    match = get_match_by_id(match_id)
    if not match:
        return None
        
    home_team = match["home_team"]
    away_team = match["away_team"]
    venue_name = match["venue"]

    all_teams = get_all_teams()
    home_stats = next((t for t in all_teams if t["team_name"] == home_team), None)
    away_stats = next((t for t in all_teams if t["team_name"] == away_team), None)

    all_venues = get_all_venues()
    venue_data = next((v for v in all_venues if v["name"] == venue_name), None)
    
    return {
        "match": match,
        "home_stats": home_stats,
        "away_stats": away_stats,
        "venue_data": venue_data
    }

def generate_with_retry(client, model, contents, config, max_retries=3):
    """Wraps the Gemini API call in an exponential backoff loop."""
    base_delay = 3
    
    for attempt in range(max_retries + 1):
        try:
            return client.models.generate_content(
                model=model,
                contents=contents,
                config=config
            )
        except Exception as e:
            if attempt == max_retries:
                print(f"Failed after {max_retries} retries: {e}")
                raise e 
          
            delay = base_delay ** (attempt + 1)
            print(f"Gemini API Error (or busy). Retrying in {delay} seconds... (Attempt {attempt + 1})")
            time.sleep(delay)


def get_match_prediction(match_id: int):

    context = build_match_context(match_id)
    if not context:
        return None

    client = genai.Client(api_key=settings.gemini_api_key)

    # ── STEP 1: Research call ──────────────────────────────────
    # Google Search is ON. No JSON schema.
    # Gemini searches for current injuries, form, squad news.
    research_prompt = f"""
You are an elite football tactical analyst with access to current squad news.
Search for the latest information on both teams before analysing.

MATCH:
{context['match']['home_team']} vs {context['match']['away_team']}
Group: {context['match']['group']}
Date: {context['match']['date']}

VENUE:
Stadium: {context['venue_data']['name']}
Altitude: {context['venue_data']['altitude_meters']}m above sea level
Climate: {context['venue_data']['summer_climate']}

{context['match']['home_team']}:
FIFA Rank: {context['home_stats']['fifa_ranking']}
Base camp: {context['home_stats']['base_camp_location']}

{context['match']['away_team']}:
FIFA Rank: {context['away_stats']['fifa_ranking']}
Base camp: {context['away_stats']['base_camp_location']}

ANALYSIS INSTRUCTIONS:
Search for and use current information on:
- Confirmed injuries and suspensions for both squads
- Expected starting XI based on recent selections
- Last 5 match results and form for each team
- Head-to-head record

Then analyse:
- Venue impact: altitude difference from base camps, climate effect on stamina
- Tactical matchup: formations, pressing style, defensive shape
- Goal threat and defensive vulnerability of each team
- Key individual battles that will decide the match
- Motivation, pressure, tournament context

STRICT RULES:
- key_players must ONLY include fit, available, expected starters
- Do NOT include any player who is injured, suspended, or out of form
- injuries list must include every known fitness concern, even doubts
- predicted_score must be your single most likely scoreline
- confidence must reflect genuine uncertainty — rarely above 0.80
"""

    try:
        research_response = generate_with_retry(
            client=client,
            model='gemini-2.5-flash',
            contents=research_prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                temperature=0.7,
            )
        )
        research_text = research_response.text


    except Exception as e:
        print(f"Error in research step: {e}")
        return None

    # ── STEP 2: Structure call ─────────────────────────────────
    # Google Search is OFF. JSON schema is ON.
    # Gemini just reorganises the research into clean JSON.
    
    structure_prompt = f"""
Convert the following football match analysis into the required JSON format.
Do not add new opinions or invent information.
Only structure what is already present in the analysis below.

ANALYSIS:
{research_text}
"""

    try:
        final_response = generate_with_retry(
            client=client,
            model='gemini-2.5-flash',
            contents=structure_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=PredictionResponse,
                temperature=0.2,
            )
        )


    except Exception as e:
        print(f"Error in structure step: {e}")
        return None

    prediction_dict = json.loads(final_response.text)
    prediction_dict["match_id"] = match_id

    return prediction_dict