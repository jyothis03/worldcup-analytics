# 🌍 World Cup AI Tactical Prediction App — Reset & Rebuild Plan

## Goal Description

The project grew too complex too quickly. The user has deleted the frontend and requested a complete reset of the backend services, data, and scripts back to "Phase 0" (the basic skeleton API). The goal is to clear out the complex code, returning to a clean slate, and then carefully rebuild the project step-by-step so the user can fully understand the data pipeline, services, and frontend architecture.

This plan serves as the handover document for the next agent to understand the current state and what needs to be built.

## Proposed Changes (The Reset)

We will strip the backend down to just the fundamental FastAPI setup.

### Backend Data & Scripts
- **[DELETE]** `backend/data/` (All static JSON files: fixtures, teams, groups, stadiums)
- **[DELETE]** `backend/scripts/` (Scripts like `fetch_static_data.py` and tests)

### Backend Services
- **[DELETE]** `backend/app/services/` (The entire services directory including `ai_service.py`, `data_service.py`, `static_data.py`, `football_api.py`)

### Backend API
- **[MODIFY]** `backend/app/api/predict.py`
  - Remove all imports to the deleted services.
  - Revert the endpoints to return simple hardcoded fake predictions to serve as a structural baseline (Phase 1).

## Next Steps For The Agent (Rebuilding)

Once the reset is complete, the next agent must proceed with the following phases, **ensuring the user understands every file created**.

### Phase 1: Rebuilding the Data Pipeline (Scripts & Data)
- **Objective:** Teach the user how to fetch and store static data.
- **Action:** Re-create `fetch_static_data.py` to pull fixtures and teams. Store them in `backend/data/`. Explain *why* we store static data (to save API calls and reduce latency).
One-time script: Fetch static World Cup 2026 data from **OpenFootball's GitHub repository** (`cup.txt`),
parse the groups and teams, algorithmically generate the group stage fixtures (since the exact schedule isn't fully published yet),
enrich it with altitude, climate, and FIFA ranking info, and save as clean JSON files in `backend/data/`.

### Phase 1.5: Enriching Static Data (Context for AI)
- **Objective:** Add context that drastically impacts real-world match outcomes so the AI can make smarter tactical predictions.
- **Action:** Create `fetch_venue_data.py`. Read the venues and teams from the generated JSONs and ask Gemini to provide:
  - **`venues.json`:** Altitude (meters) and Summer Climate (e.g., Hot/Humid). (Altitude heavily impacts stamina; heat impacts pacing).
  - **`team_stats.json`:** Pre-tournament FIFA rankings and their World Cup Training Center (Base Camp) location. (Base camp location is great for calculating travel fatigue to matches).

### Phase 2: Rebuilding the Services
- **Objective:** Teach the user how backend business logic works.
- **Action:** 
  1. Create `data_service.py` to read from the JSON files.
  2. Create `ai_service.py` to handle the Google Gemini API integration. Explain how the context is structured before sending it to the LLM.

### Phase 3: Connecting the API
- **Objective:** Hook the services back into the FastAPI router.
- **Action:** Update `predict.py` to use `data_service` and `ai_service` instead of hardcoded stubs. 

### Phase 4: Rebuilding the Frontend
- **Objective:** Teach the user React fundamentals while building the UI.
- **Action:** Scaffold a new Vite/React frontend. Build components one by one (Navbar, Match List, Prediction Card), explaining hooks (`useState`, `useEffect`) and API fetching.

## User Review Required

> [!WARNING]  
> Approving this plan will completely wipe the existing `services`, `data`, and `scripts` folders from your backend, and reset your prediction API to a blank slate.
>
> If you are ready to start fresh, approve this plan, and I will execute the deletions. Then, you can ask me (or the next agent) to begin Phase 1 of the rebuild!
