from fastapi import APIRouter, Query, HTTPException
from backend.app.services.data_service import get_all_matches, get_match_by_id, get_all_teams, get_all_venues
from backend.app.services.ai_service import get_match_prediction

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
def predict_match(match_id: int):
    """Predicts a match using Gemini AI and our structured data."""
    prediction = get_match_prediction(match_id)

    if not prediction:
        raise HTTPException(status_code=404, detail=f"Prediction failed.")
        
    return prediction