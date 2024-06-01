import numpy as np
from flask import request, jsonify
from config import app, ALLOWED_EXTENSIONS
from models import create_team_data_frame

team_df = create_team_data_frame()

# gets the total amount of goals scored in the league
def total_league_goals():
    total_goals = 0
    for index, row in team_df.iterrows():
        goals_scored = row['GF']
        total_goals += goals_scored
    return total_goals

# gets the total amount of matches played in the league
def total_matches_played():
    total_matches = 0
    for index, row in team_df.iterrows():
        matches_played = row['MP']
        total_matches += matches_played
    return total_matches

# gets the average goals per match for the entire league
def avg_league_goals():
    league_goals = total_league_goals()
    matches_played = total_matches_played()
    return league_goals/matches_played

# gets the attack rating for a specified team
def att_rating(team_name):
    selected_team = team_df.loc[team_name]
    goals_scored = selected_team['GF']
    matches_played = selected_team['MP']
    att_rating = (goals_scored/matches_played)/avg_league_goals()
    return att_rating

# gets the defense rating for a specified team
def def_rating(team_name):
    selected_team = team_df.loc[team_name]
    goals_conceded = selected_team['GA']
    matches_played = selected_team['MP']
    def_rating = (goals_conceded/matches_played)/avg_league_goals()
    return def_rating

# gets the expected goals for both teams in a head-to-head
def expected_goals(home_team, away_team):
    home_att_rating = att_rating(home_team)
    home_def_rating = def_rating(home_team)
    away_att_rating = att_rating(away_team)
    away_def_rating = def_rating(away_team)
    home_xG = home_att_rating * away_def_rating * avg_league_goals()
    away_xG = away_att_rating * home_def_rating * avg_league_goals()
    return home_xG, away_xG

# creates a dictionary out of the poisson distribution
def dist_to_dict(dist):
    new_dict = {}
    for i in range(11):
        i_list = [num for num in dist if num == i]
        i_prob = len(i_list)/len(dist)
        new_dict[i] = i_prob
    return new_dict
 
# route that gets all the teams
@app.route('/teams', methods=['GET'])
def get_teams():
    return jsonify(team_df.to_dict(orient='records')), 200

# route that gets the data for the specified team
@app.route('/teams/<team_name>', methods=['GET'])
def get_team(team_name):
    selected_team = team_df[team_df['Team'] == team_name]
    return jsonify(selected_team.to_dict(orient='records')), 200

# route that gets the attack and defense ratings for the specified team
@app.route('/teams/ratings/<team_name>', methods=['GET'])
def get_ratings(team_name):
    team_att_rating = att_rating(team_name)
    team_def_rating = def_rating(team_name)
    ratings = {'attRating': team_att_rating, 'defRating': team_def_rating}
    return jsonify(ratings), 200

# route that gets the expected goals in a head-to-head between 2 specified teams
@app.route('/match/custom/xG/<home_team>/<away_team>', methods=['GET'])
def get_xG(home_team, away_team):
    home_expected_goals, away_expected_goals = expected_goals(home_team, away_team)
    results = {'homeXG': home_expected_goals, 'awayXG': away_expected_goals}
    return jsonify(results), 200

# route that gets the probability of both teams scoring a certain amount of goals
@app.route('/match/custom/probs/<home_team>/<away_team>', methods=['GET'])
def get_probs(home_team, away_team):
    home_XG, away_XG = expected_goals(home_team, away_team)
    home_dist = np.random.poisson(lam=home_XG, size=1000)
    away_dist = np.random.poisson(lam=away_XG, size=1000)
    home_dict = dist_to_dict(home_dist)
    away_dict = dist_to_dict(away_dist)
    probs = {'homeProbs': home_dict, 'awayProbs': away_dict}
    return jsonify(probs), 200

if __name__ == "__main__":
    with app.app_context():
        pass
    app.run(debug=True)