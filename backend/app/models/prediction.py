from pydantic import BaseModel, Field

class PlayerInjury(BaseModel):
    player_name: str
    injury_detail: str          # e.g. "Hamstring strain, doubtful"

class KeyBattle(BaseModel):
    home_player: str
    away_player: str
    analysis: str

class TeamPrediction(BaseModel):
    name: str
    expected_formation: str
    key_players: list[str]      # ONLY fit, in-form, expected starters
    injuries: list[PlayerInjury]
    recent_form: str
    tactical_approach: str

class ScorePrediction(BaseModel):
    home: int
    away: int

class WinProbability(BaseModel):
    home: float
    draw: float
    away: float

class PredictionResponse(BaseModel):
    home_team: TeamPrediction
    away_team: TeamPrediction
    predicted_score: ScorePrediction
    scoreline_range: str            
    confidence: float               # 0.0 to 1.0
    win_probability: WinProbability      
    venue_impact: str               # altitude + climate analysis
    tactical_analysis: str          # full matchup breakdown
    key_battles: list[KeyBattle]
    reasoning: str                  # final verdict paragraph