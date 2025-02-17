import json
from bson import json_util
from flask import Blueprint, jsonify
from config import fixture_db
from routes.status import set_gameweek_status

fixtures_routes = Blueprint('fixture', __name__)

@fixtures_routes.route('/api/fixtures', methods=['GET'])
def get_fixtures():
    """Gets all the fixtures for the season"""
    try:
        fixtures = fixture_db.find({}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures: {e}'}), 404
    
@fixtures_routes.route('/api/fixtures/next', methods=['GET'])
def get_next_fixture():
    """Gets the most recent upcoming fixture in the season"""
    try:
        next_fixture = fixture_db.find({}, {"_id": 0})[0]
        json_next_fixtures = json.loads(json_util.dumps(next_fixture))
        return jsonify(json_next_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get next fixture: {e}'}), 404
    
@fixtures_routes.route('/api/fixtures/gameweek/<int:gameweek_id>', methods=['GET'])
def get_gameweek_fixtures(gameweek_id: int):
    """Gets all the fixtures for the specified gameweek"""
    try:
        gameweek_fixtures = fixture_db.find({'Gameweek': gameweek_id}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(gameweek_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get gameweek "{gameweek_id}": {e}'}), 404
    
@fixtures_routes.route('/api/fixtures/gameweek/current', methods=['GET'])
def get_current_gameweek():
    """Gets all the fixtures for the current gameweek"""
    try:
        gameweek_fixtures = fixture_db.find({'Gameweek': set_gameweek_status()[0]}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(gameweek_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get gameweek "{set_gameweek_status()[0]}": {e}'}), 404
    
@fixtures_routes.route('/api/fixtures/gameweek/next', methods=['GET'])
def get_next_gameweek():
    """Gets all the fixtures for the next gameweek"""
    try:
        gameweek_fixtures = fixture_db.find({'Gameweek': set_gameweek_status()[1]}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(gameweek_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get gameweek "{set_gameweek_status()[1]}": {e}'}), 404
    
@fixtures_routes.route('/api/fixtures/<team>', methods=['GET'])
def get_team_fixtures(team: str):
    """Gets all the fixtures for the specified team"""
    try:
        team_fixtures = fixture_db.find({'$or': [{'Home': team}, {'Away': team}]}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(team_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures for "{team}": {e}'}), 404