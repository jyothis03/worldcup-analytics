from __future__ import annotations
from pydantic import BaseModel

class TeamData(BaseModel):
    team_id: int
    name: str
    country: str
    fifa_ranking: int
    climate_origin: str = "unknown"  # "cool temperate", "hot arid", etc.

class VenueInfo(BaseModel):
    stadium: str
    city: str
    country: str
    altitude_m: int = 0
    capacity: int = 0

class MatchData(BaseModel):
    match_id: int
    date: str
    competition: str
    stage: str  # "Group A", "Round of 16", "Quarter-final"
    team_a: TeamData
    team_b: TeamData
    venue: VenueInfo
