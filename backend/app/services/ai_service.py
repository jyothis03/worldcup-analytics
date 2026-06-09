from google import genai
from google.genai import types
import json
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

def get_match_prediction(match_id: int):

    context= build_match_context(match_id)
    if not context:
        return None

    api_key = settings.gemini_api_key
    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are an elite football tactical analyst predicting World Cup 2026 matches.
    
    MATCH DETAILS:
    - {context['match']['home_team']} vs {context['match']['away_team']}
    - Group: {context['match']['group']}
    
    VENUE IMPACT:
    - Playing at: {context['venue_data']['name']}
    - Altitude: {context['venue_data']['altitude_meters']} meters above sea level
    - Expected Climate: {context['venue_data']['summer_climate']}
    
    HOME TEAM ({context['match']['home_team']}):
    - FIFA Rank: {context['home_stats']['fifa_ranking']}
    - Base Camp: {context['home_stats']['base_camp_location']}
    
    AWAY TEAM ({context['match']['away_team']}):
    - FIFA Rank: {context['away_stats']['fifa_ranking']}
    - Base Camp: {context['away_stats']['base_camp_location']}
    
    INSTRUCTIONS:
    Analyze how the altitude, climate, and travel from their base camps will impact stamina.
    Also how different is the altitude from their base camps and analyse if it will be impactful. 
    Analyze the tactical matchup based on their FIFA rankings, recent form, injuries, current squad strength,
    goal scoring tendency, goal conceding tendency, h2h results, expected 11, motivation, pressure, historical squad strengths etc and anything relevant.
    Predict the final score and identify the key tactical battles.
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=PredictionResponse,
                temperature=0.7
            ),
        )
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return None

    prediction_dict = json.loads(response.text)
    
    prediction_dict["match_id"] = match_id 
    
    return prediction_dict    