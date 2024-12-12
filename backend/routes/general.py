from flask import Blueprint, jsonify
from config import team_db, fixture_db
from scraper import scrape_team_data, scrape_fixture_data

general_routes = Blueprint('general', __name__)

@general_routes.route('/update/teams', methods=['GET', 'POST'])
def update_team_database():
    try:
        team_db.delete_many({})
        teams = scrape_team_data()
        team_db.insert_many(teams)
        return jsonify({'message': 'Teams created/updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not update the team database: {e}'})

@general_routes.route('/update/fixtures', methods=['GET', 'POST'])
def update_fixture_database():
    try:
        fixture_db.delete_many({})
        fixtures = scrape_fixture_data()
        fixture_db.insert_many(fixtures)
        return jsonify({'message': 'Fixtures created/updated successfully!'}), 200
    except Exception as e:
        return jsonify({'error_msg': f'Could not update the fixture database: {e}'})