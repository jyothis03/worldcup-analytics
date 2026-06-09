from pydantic import BaseModel


class TeamInfo(BaseModel):
    name: str
    recent_form: str
    key_players: list[str]


class PredictionResponse(BaseModel):
    match_id: int
    team_a: TeamInfo
    team_b: TeamInfo
    predicted_score: str
    confidence: float
    tactical_analysis: str
    key_battles: list[str]
    reasoning: str
