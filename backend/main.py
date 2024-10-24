import numpy as np
from flask import jsonify
from config import app, db
from models import Team
from scraper import teams_dict


# DB FUNCTIONS --------------------------------------------------------------------------------------------------------------------------------


def reset():
    """Deletes all the records from the database"""
    teams = Team.query.all()
    for team in teams:
        db.session.delete(team)
    db.session.commit()


def populate():
    """Adds new records to the database"""
    teams = teams_dict()

    for i in range(len(teams)):
        team_name = teams[i]['Squad']
        matches_played = teams[i]['MP']
        wins = teams[i]['W']
        draws = teams[i]['D']
        losses = teams[i]['L']
        goals_scored = teams[i]['GF']
        goals_conceded = teams[i]['GA']
        goal_difference = teams[i]['GD']

        new_team = Team(
            team_name=team_name,
            matches_played=matches_played,
            wins=wins,
            draw=draws,
            loss=losses,
            goals_scored=goals_scored,
            goals_conceded=goals_conceded,
            goal_difference=goal_difference
        )

        try:
            db.session.add(new_team)
            db.session.commit()
        except Exception as e:
            return jsonify({'message': str(e)}), 400
        

def update():
    reset()
    populate()


# APP FUNCTIONS -------------------------------------------------------------------------------------------------------------------------------


def total_league_goals() -> int:
    """Calulates the sum of the number of goals scored for each team"""
    league_goals = 0
    teams = Team.query.all()
    team_goals = [team.goals_scored for team in teams]
    league_goals = np.sum(team_goals)
    return league_goals


def total_matches_played() -> int:
    """Calculates the sum of the number of matches played for each team"""
    matches_played = 0
    teams = Team.query.all()
    team_matches = [team.matches_played for team in teams]
    matches_played = np.sum(team_matches)
    return matches_played


def avg_league_goals() -> float:
    """Calculates the average amount of goals scored league-wide"""
    league_goals = total_league_goals()
    matches_played = total_matches_played()
    average = league_goals / matches_played
    return average


def att_rating(team_name: str) -> float:
    """Calculates the offensive rating of the given team"""
    selected_team: Team = Team.query.filter_by(team_name=team_name).first()
    goals_scored = selected_team.goals_scored
    matches_played = selected_team.matches_played
    att_rating = (goals_scored / matches_played) / avg_league_goals()
    return att_rating


def def_rating(team_name: str) -> float:
    """Claculates the defensive rating of the given team"""
    selected_team: Team = Team.query.filter_by(team_name=team_name).first()
    goals_conceded = selected_team.goals_conceded
    matches_played = selected_team.matches_played
    def_rating = (goals_conceded / matches_played) / avg_league_goals()
    return def_rating


def expected_goals(home_team: str, away_team: str) -> tuple:
    """Calculates the expected goals for two given teams in a head-to-head"""
    home_att_rating = att_rating(home_team)
    home_def_rating = def_rating(home_team)
    away_att_rating = att_rating(away_team)
    away_def_rating = def_rating(away_team)
    home_xG = home_att_rating * away_def_rating * avg_league_goals()
    away_xG = away_att_rating * home_def_rating * avg_league_goals()
    return home_xG, away_xG


def dist_to_dict(dist) -> dict:
    """Converts a poisson distribution to dictionary format"""
    new_dict = {}
    for i in range(11):
        i_list = [num for num in dist if num == i]
        i_prob = len(i_list)/len(dist)
        new_dict[i] = i_prob
    return new_dict


# DB ROUTES -----------------------------------------------------------------------------------------------------------------------------------



@app.route('/update', methods=['POST'])
def update_database():
    """Removes all the records from the database and adds new items"""
    update()
    return jsonify({'message': 'Database successfully updated.'}), 200


# APP ROUTES ----------------------------------------------------------------------------------------------------------------------------------


@app.route('/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    json_teams = list(map(lambda x: x.to_json(), teams))
    return jsonify({'teams': json_teams}), 200


@app.route('/teams/<team_name>', methods=['GET'])
def get_team(team_name: str):
    """Gets a team from the database using the given team name"""
    selected_team: Team = Team.query.filter_by(team_name=team_name).first()
    if not selected_team:
        return jsonify({'message': 'Team not found.'}), 404
    json_team = selected_team.to_json()
    return jsonify({'team': json_team}), 200


@app.route('/ratings/<team_name>', methods=['GET'])
def get_team_rating(team_name: str):
    """Calculates the offensive and defensive ratings for the given team"""
    team_att_rating = att_rating(team_name)
    team_def_rating = def_rating(team_name)
    ratings = {'att_rating': team_att_rating, 'def_rating': team_def_rating}
    return jsonify(ratings), 200


@app.route('/xG/<home_team>/<away_team>', methods=['GET', 'POST'])
def get_xG(home_team: str, away_team: str):
    """Calculates the xG for the given home and away teams"""
    home_xG, away_xG = expected_goals(home_team, away_team)
    results = {'home_xG': home_xG, 'away_xG': away_xG}
    return jsonify(results), 200


@app.route('/probability/<home_team>/<away_team>', methods=['GET', 'POST'])
def get_probs(home_team: str, away_team: str):
    """Calculates the probailities of the given teams scoring 1-10 goals in a head-to-head"""
    home_xG, away_xG = expected_goals(home_team, away_team)
    home_dist = np.random.poisson(lam=home_xG, size=1000)
    away_dist = np.random.poisson(lam=away_xG, size=1000)
    home_dict = dist_to_dict(home_dist)
    away_dict = dist_to_dict(away_dist)
    probs = {'home_probs': home_dict, 'away_probs': away_dict}
    return jsonify(probs), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        update()
    app.run(debug=True)