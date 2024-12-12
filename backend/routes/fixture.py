import json
from bson import json_util
from flask import Blueprint, jsonify
from config import fixture_db

fixture_routes = Blueprint('fixture', __name__)

@fixture_routes.route('/fixtures', methods=['GET'])
def get_fixtures():
    try:
        fixtures = fixture_db.find({})
        json_fixtures = json.loads(json_util.dumps(fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures: {e}'})

@fixture_routes.route('/fixtures/<int:gameweek_id>', methods=['GET'])
def get_gameweek_fixtures(gameweek_id: int):
    try:
        gameweek_fixtures = fixture_db.find({'Gameweek': gameweek_id})
        json_fixtures = json.loads(json_util.dumps(gameweek_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get gameweek "{gameweek_id}": {e}'})

@fixture_routes.route('/fixtures/<team>', methods=['GET'])
def get_team_fixtures(team: str):
    try:
        team_fixtures = fixture_db.find({'$or': [{'Home': team}, {'Away': team}]})
        json_fixtures = json.loads(json_util.dumps(team_fixtures))
        return jsonify(json_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get fixtures for "{team}": {e}'})
    
@fixture_routes.route('/fixtures/next', methods=['GET'])
def get_next_fixture():
    try:
        next_fixture = fixture_db.find({'Score': ' - '})
        json_next_fixtures = json.loads(json_util.dumps(next_fixture))
        return jsonify(json_next_fixtures), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not get next fixture: {e}'})