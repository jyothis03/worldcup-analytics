from google import genai
from backend.app.core.config import settings
from backend.app.services.data_service import get_match_by_id, get_all_teams, get_all_venues

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