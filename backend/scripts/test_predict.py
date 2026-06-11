import os
import sys
import json
sys.path.append(".")
from dotenv import load_dotenv
load_dotenv()

from backend.app.services.ai_service import get_match_prediction

# Using Iraq vs Norway (Match 21, or let's use match 20 Australia vs Turkey)
prediction = get_match_prediction(20)
with open("prediction_output_debug.json", "w", encoding="utf-8") as f:
    json.dump(prediction, f, indent=2)
print("Saved to prediction_output_debug.json")
