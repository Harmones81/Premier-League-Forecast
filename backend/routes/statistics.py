import json
import numpy as np
from bson import json_util
from flask import Blueprint, jsonify
from config import team_db

statistics_route = Blueprint('statistics', __name__)

def total_league_goals() -> int:
    try:
        teams = team_db.find({})
        goals = [team['GF'] for team in teams]
        league_goals = int(np.sum(goals))
        return league_goals
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the total league goals: {e}'})
    
def total_matches_played() -> int:
    try:
        teams = team_db.find({})
        matches = [team['MP'] for team in teams]
        matches_played = int(np.sum(matches))
        return matches_played
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the total matches played: {e}'})
    
def avg_league_goals() -> float:
    try:
        league_goals = total_league_goals()
        matches_played = total_matches_played()
        average = league_goals / matches_played
        return average
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the average league goals: {e}'})
    
def att_rating(team: str) -> float:
    try:
        selected_team = team_db.find_one({'Team': team})
        goals_scored = selected_team['GF']
        matches_played = selected_team['MP']
        att_rating = (goals_scored / matches_played) / avg_league_goals()
        return att_rating
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the attack rating for "{team}": {e}'})
    
def def_rating(team: str) -> float:
    try:
        selected_team = team_db.find_one({'Team': team})
        goals_allowed = selected_team['GA']
        matches_played = selected_team['MP']
        def_rating = (goals_allowed / matches_played) / avg_league_goals()
        return def_rating
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the defensive rating for "{team}": {e}'})

# TODO - Fix this error
@statistics_route.route('/statistics', methods=['GET'])
def get_league_statistics():
    try:
        league_goals = total_league_goals()
        matches_played = total_matches_played()
        avg_goals = avg_league_goals()

        statistics = {
            'league_goals': league_goals,
            'matches_played': matches_played,
            'avg_goals': avg_goals
        }

        json_statistics = json.loads(json_util.dumps(statistics))
        return jsonify(json_statistics), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get statistics: {e}'})

@statistics_route.route('/statistics/<team_name>', methods=['GET'])
def get_team_statistics(team_name: str):
    try:
        a_rating = att_rating(team_name)
        d_rating = def_rating(team_name)

        team_statistics = {
            'att_rating': a_rating,
            'def_rating': d_rating,
        }

        json_statistics = json.loads(json_util.dumps(team_statistics))
        return jsonify(json_statistics), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get statistics for "{team_name}": {e}'})