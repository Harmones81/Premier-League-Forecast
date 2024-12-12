import numpy as np
from flask import Blueprint, jsonify
from routes.statistics import att_rating, def_rating, avg_league_goals

predictions_route = Blueprint('predictions', __name__)

def expected_goals(home_team: str, away_team: str) -> tuple[float, float]:
    home_att_rating = att_rating(home_team)
    home_def_rating = def_rating(home_team)
    away_att_rating = att_rating(away_team)
    away_def_rating = def_rating(away_team)
    home_xG = home_att_rating * away_def_rating * avg_league_goals()
    away_xG = away_att_rating * home_def_rating * avg_league_goals()
    return home_xG, away_xG

def dist_to_dict(dist) -> dict:
    new_dict = {}
    for i in range(11):
        i_list = [num for num in dist if num == i]
        i_prob = len(i_list)/len(dist)
        new_dict[i] = i_prob
    return new_dict

def predicted_scoreline(home_team: str, away_team: str) -> tuple[int, int]:
    home_xG, away_xG = expected_goals(home_team, away_team)
    home_score = round(home_xG)
    away_score = round(away_xG)
    return home_score, away_score

@predictions_route.route('/predictions/xG/<home_team>/<away_team>', methods=['GET'])
def get_xG(home_team: str, away_team: str):
    home_xG, away_xG = expected_goals(home_team, away_team)
    results = {'home_xG': home_xG, 'away_xG': away_xG}
    return jsonify(results), 200

@predictions_route.route('/predictions/dist/<home_team>/<away_team>', methods=['GET'])
def get_dist(home_team: str, away_team: str):
    home_xG, away_xG = expected_goals(home_team, away_team)
    home_dist = np.random.poisson(lam=home_xG, size=1000)
    away_dist = np.random.poisson(lam=away_xG, size=1000)
    home_dict = dist_to_dict(home_dist)
    away_dict = dist_to_dict(away_dist)
    probs = {'home_dist': home_dict, 'away_dist': away_dict}
    return jsonify(probs), 200

@predictions_route.route('/predictions/score/<home_team>/<away_team>', methods=['GET'])
def get_scoreline(home_team: str, away_team: str):
    home_score, away_score = predicted_scoreline(home_team, away_team)
    scoreline = {'home_score': home_score, 'away_score': away_score}
    return jsonify(scoreline), 200