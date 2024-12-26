import json
from bson import json_util
from flask import Blueprint, jsonify
from config import fixture_db

fixture_routes = Blueprint('fixture', __name__)

@fixture_routes.route('/api/fixtures', methods=['GET'])
def get_fixtures():
    """Gets all the fixtures for the season"""
    try:
        fixtures = fixture_db.find({}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures: {e}'})
    
@fixture_routes.route('/api/fixtures/next', methods=['GET'])
def get_next_fixture():
    try:
        next_fixture = [doc for doc in fixture_db.find({'Result': '-'}, {"_id": 0})][0]
        json_next_fixtures = json.loads(json_util.dumps(next_fixture))
        return jsonify(json_next_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get next fixture: {e}'})

@fixture_routes.route('/api/fixtures/gameweek/<int:gameweek_id>', methods=['GET'])
def get_gameweek_fixtures(gameweek_id: int):
    """Gets all the fixtures for the specified gameweek"""
    try:
        gameweek_fixtures = fixture_db.find({'Gameweek': gameweek_id}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(gameweek_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get gameweek "{gameweek_id}": {e}'})

@fixture_routes.route('/api/fixtures/played', methods=['GET'])
def get_played_fixtures():
    try:
        played_fixtures = fixture_db.find({'Result': {'$ne': '-'}}, {"_id": 0})
        json_played_fixtures = json.loads(json_util.dumps(played_fixtures))
        return jsonify(json_played_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get played fixtures: {e}'})
    
@fixture_routes.route('/api/fixtures/unplayed', methods=['GET'])
def get_unplayed_fixtures():
    try:
        unplayed_fixtures = fixture_db.find({'Result': '-'}, {"_id": 0})
        json_unplayed_fixtures = json.loads(json_util.dumps(unplayed_fixtures))
        return jsonify(json_unplayed_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get unplayed fixtures: {e}'})

@fixture_routes.route('/api/fixtures/<team>', methods=['GET'])
def get_team_fixtures(team: str):
    """Gets all the fixtures for the specified team"""
    try:
        team_fixtures = fixture_db.find({'$or': [{'Home': team}, {'Away': team}]}, {"_id": 0})
        json_fixtures = json.loads(json_util.dumps(team_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures for "{team}": {e}'})