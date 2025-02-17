import json
from bson import json_util
from flask import Blueprint, jsonify
from config import team_db

team_routes = Blueprint('team', __name__)

@team_routes.route('/api/teams', methods=['GET'])
def get_teams():
    """Get all the teams in the database"""
    try:
        teams = team_db.find({}, {"_id": 0})
        json_teams = json.loads(json_util.dumps(teams))
        return jsonify(json_teams), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get teams: {e}'}), 404

@team_routes.route('/api/teams/<team_name>', methods=['GET'])
def get_team(team_name: str):
    """Get the specified team from the database"""
    try:
        teams = team_db.find_one({'Team': team_name}, {"_id": 0})
        json_team = json.loads(json_util.dumps(teams))
        return jsonify(json_team), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get team "{team_name}": {e}'}), 404