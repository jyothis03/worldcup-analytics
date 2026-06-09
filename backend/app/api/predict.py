from fastapi import APIRouter, Query
from backend.app.services.data_service import get_all_matches, get_match_by_id

router = APIRouter(prefix="/api/v1", tags=["predictions"])

@router.get("/matches")
def get_matches():
    matches = get_all_matches()
    return {"matches": matches}

@router.get("/match/{match_id}")
async def get_match_detail(match_id: int):
    """Get detailed static data for a specific match. Currently returning dummy data."""
    return {
        "id": match_id,
        "home_team": "Brazil",
        "away_team": "France",
        "venue": "MetLife Stadium",
        "date": "2026-06-15T18:00:00Z",
        "group": "Group A",
        "type": "Group Stage",
        "home_team_fifa_rank": 3,
        "away_team_fifa_rank": 2,
        "climate": "Humid",
        "altitude_meters": 0
    }

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
