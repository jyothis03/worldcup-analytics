import json
from pathlib import Path
from functools import lru_cache

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"

@lru_cache()
def load_json_file(filename: str):
    file_path = DATA_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Missing essential data file: {filename}")
        
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_all_matches():
    return load_json_file("fixtures.json")

def get_match_by_id(match_id: int):
    matches = get_all_matches()
    for match in matches:
        if match["id"] == match_id:
            return match
    return None

def get_all_teams():
    return load_json_file("team_stats.json")

def get_all_venues():
    return load_json_file("venues.json")
