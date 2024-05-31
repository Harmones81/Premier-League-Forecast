# Premier League Forecast

Premier League Forecast is a dynamic web application that provides users with insightful predictions and analytics for current Premier League players and upcoming matches.

## Table of Contents
- [Features](#features)
- [Backend Routes](#backend-routes)
- [Setup/Run Locally](#setuprun-locally)

## Features
- **Match Predictions:** Get predictions for upcoming Premier League matches.
- **Team Statistics:** View detailed statistics for each Premier League team.
- **Player Performance:** Analyze performance metrics for individual players.

## Backend Routes

### Match Routes
- `GET /matches/upcoming`
  - Retrieves a list of upcoming matches.

- `GET /matches/predict/:match_id`
  - Predicts the outcome of a specific match.
  - **Parameters:** `match_id` - The ID of the match.

### Team Routes
- `GET /teams`
  - Retrieves a list of all current Premier League teams.

- `GET /teams/:team_name`
  - Retrieves detailed statistics for a specific team.
  - **Parameters:** `team_name` - The name of the team.

### Player Routes
- `GET /players`
  - Retrieves a list of all the current players in the Premier League.

- `GET /players/:player_name`
  - Retrieves performance metrics (stats) for a specific player.
  - **Parameters:** `player_name` - The name of the player.
    
- `GET /players/predict/:player_name`
  - Predicts the amount of FPL points a player will get in the upcoming gameweek.
  - **Parameters:** `player_name` - The name of the player.

## Setup/Run Locally

### Prerequisites
- Python 3.x
- Node.js
- npm (Node Package Manager)
- Flask & Flask CORS

### Backend Setup (Flask)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Harmones81/premier-league-forecast.git
   cd premier-league-forecast

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install backend dependencies**
   ```bash
   - navigate to backend directory
   - pip3 install -r requirements.txt

4. **Run the flask app**
   ```bash
   python main.py
   
### Frontend Setup (React)
1. **Navigate to frontend directory**
   ```bash
   cd frontend

2. **Install frontend dependencies**
   ```bash
   npm install

3. **Run the react app**
   ```bash
   npm run dev
