from fastapi import APIRouter, Query, HTTPException
from backend.app.services.data_service import get_all_matches, get_match_by_id, get_all_teams, get_all_venues


router = APIRouter(prefix="/api/v1", tags=["predictions"])

@router.get("/matches")
def get_matches():
    matches = get_all_matches()
    return {"matches": matches}

@router.get("/match/{match_id}")
def get_match_detail(match_id: int):
    match = get_match_by_id(match_id)
    if not match:
        raise HTTPException(status_code=404, detail=f"Match with ID {match_id} not found")
    return match

@router.get("/teams")
def get_teams():
    """Returns the list of all teams and their stats"""
    return {"teams": get_all_teams()}

@router.get("/venues")
def get_venues():
    """Returns the list of all venues and their climate/altitude"""
    return {"venues": get_all_venues()}


@router.get("/predict")
async def predict(match_id: int = Query(..., description="The ID of the match to predict")):
    """Predict a match. Currently returning a hardcoded fake prediction (Phase 1)."""
    return {
        "match_id": match_id,
        "prediction_text": "France will dominate the midfield but Brazil's counter-attacks will be lethal.",
        "predicted_score": {
            "home": 2,
            "away": 1
        },
        "confidence": 0.65,
        "win_probability": {
            "home": 0.55,
            "away": 0.25,
            "draw": 0.20
        },
        "key_battles": [
            {
                "home_player": "Vinicius Jr",
                "away_player": "Kounde",
                "importance": 0.9,
                "analysis": "Pivotal battle on the flank."
            }
        ],
        "recent_form": {
            "home": ["W", "W", "D", "W", "W"],
            "away": ["W", "D", "W", "W", "D"]
        },
        "tactical_analysis": {
            "home_formation": "4-2-3-1",
            "away_formation": "4-3-3",
            "expected_scenario": "High-paced game with lots of transitions.",
            "key_risks": ["Brazil's fullbacks leaving space behind."]
        }
    }
