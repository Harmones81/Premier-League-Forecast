import json
import numpy as np
from bson import json_util
from flask import Blueprint, jsonify
from config import team_db

statistics_route = Blueprint('statistics', __name__)

def total_league_goals() -> int:
    """Calculate the total goals scored in the league"""
    try:
        teams = team_db.find({}, {"_id": 0})
        goals = [team['GF'] for team in teams]
        league_goals = int(np.sum(goals))
        return league_goals
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the total league goals: {e}'}), 404
    
def total_matches_played() -> int:
    """Calculate the total matches played in the league"""
    try:
        teams = team_db.find({}, {"_id": 0})
        matches = [team['MP'] for team in teams]
        matches_played = int(np.sum(matches))
        return matches_played
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the total matches played: {e}'}), 404
    
def avg_league_goals() -> float:
    """Calculate the average goals scored per match in the league"""
    try:
        league_goals = total_league_goals()
        matches_played = total_matches_played()
        average = league_goals / matches_played
        return average
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the average league goals: {e}'}), 404
    
def att_rating(team: str) -> float:
    """Calculates the attack rating for the specified team"""
    try:
        selected_team = team_db.find_one({'Team': team}, {"_id": 0})
        goals_scored = selected_team['GF']
        matches_played = selected_team['MP']
        att_rating = (goals_scored / matches_played) / avg_league_goals()
        return att_rating
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the attack rating for "{team}": {e}'}), 404
    
def def_rating(team: str) -> float:
    """Calculates the defensive rating for the specified team"""
    try:
        selected_team = team_db.find_one({'Team': team}, {"_id": 0})
        goals_allowed = selected_team['GA']
        matches_played = selected_team['MP']
        def_rating = (goals_allowed / matches_played) / avg_league_goals()
        return def_rating
    except Exception as e:
        return jsonify({'error_msg': f'Could not get the defensive rating for "{team}": {e}'}), 404

@statistics_route.route('/api/statistics', methods=['GET'])
def get_league_statistics():
    """Provides league statistics"""
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
        return jsonify({'error_msg': f'Could not get statistics: {e}'}), 404

@statistics_route.route('/api/statistics/<team_name>', methods=['GET'])
def get_team_statistics(team_name: str):
    """Provides statistics for the specified team"""
    try:
        a_rating = f'{att_rating(team_name):.2f}'
        d_rating = f'{def_rating(team_name):.2f}'

        team_statistics = {
            'att_rating': a_rating,
            'def_rating': d_rating,
        }

        json_statistics = json.loads(json_util.dumps(team_statistics))
        return jsonify(json_statistics), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get statistics for "{team_name}": {e}'}), 404