# Premier League Forecast

## Overview

Premier League Forecast is a web application that uses standard analytical data to predict the scoreline for upcoming Premier League fixtures. The application is built using:

- **Flask (backend)**
- **MongoDB (database)**
- **React (frontend)**

## Features

- Predict the scoreline for upcoming Premier League fixtures, including other statistics such as goal distributions.
- View detailed statistics for each Premier League team, such as attack rating, defense rating, and more.
- Very interactive, professional, and user-friendly UI that functions properly on both desktop and mobile devices.
- Real-time data updates that can highlight the very next fixture in the current Premier League season.

## Tech Stack

- **Backend**: Flask (Python) was used for the backend since the scope of the project is relatively small and Python offers tons of modules for scraping and data analysis.
- **Database**: MongoDB was used as the database because of its ease of use and NoSQL schema allowing for experimentation and manipulation of how data is stored.
- **Frontend**: React (Vite) was used as the frontend since its ease of use and overall flexibility can allow for future expansions for the application.

## Installation

To use/test the application, make sure you have these installed:

- Python (>= 3.8)
- Node.js & npm
- MongoDB

## Set-up

**Backend (Flask)**

1. Clone the repository
   > git clone https://github.com/yourusername/premier-league-forecast.git
   > cd premier-league-forecast
   
2. Navigate to the backend folder, create a virtual environment, and activate it
   > cd backend
   > python -m venv .venv
   > source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   
3. Install backend dependencies
   > pip install -r requirements.txt

4. Set up your MongoDB connection by running a local MongoDB instance and adding a .env file with your MongoDB connection string
   
5. Run the Flask server
   > python main.py

**Frontend (React)**

1. Navigate to the frontend directory
   > cd frontend

2. Install dependencies
   > npm install
   > npm install react-icons --save

3. Start the React app
   > npm run dev

## API Endpoints

### Database

- `/api/update/teams` - Updates the teams collection in the database
- `/api/update/fixtures` - Updates the fixtures collection in the database

### Fixtures

- **GET** `/api/fixtures` - Retrieves all the fixtures in the fixtures collection
- **GET** `/api/fixtures/next` - Retrieves the first upcoming fixture in the fixtures collection
- **GET** `/api/fixtures/gameweek/<gameweek_id>` - Retrieves the fixtures from the specified gameweek
- **GET** `/api/fixtures/gameweek/current` - Retrieves the fixtures from the current gameweek
- **GET** `/api/fixtures/gameweek/next` - Retrieves the fixtures from the next gameweek
- **GET** `api/fixtures/<team>` - Retrieves all the fixtures for the specified team

