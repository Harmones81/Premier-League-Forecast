import pandas as pd

teams_url = 'https://www.skysports.com/premier-league-table'
fixtures_url = 'https://fixturedownload.com/results/epl-2024'

def scrape_team_data() -> list[dict]:
    teams = pd.read_html(teams_url)[0]
    teams.drop('Position', axis=1, inplace=True)
    teams.columns = ['Team', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
    teams_dict = teams.to_dict(orient='records')
    return teams_dict

def scrape_fixture_data() -> list[dict]:
    fixtures = pd.read_html(fixtures_url)[0]
    edit_fixture_data(fixtures)
    fixtures.columns = ['Gameweek', 'Date', 'Location', 'Home Team', 'Away Team', 'Result']
    fixtures[['Date', 'Time']] = fixtures['Date'].str.split(' ', expand=True)
    fixtures = fixtures[fixtures['Result'] == '-']
    fixtures.drop('Result', axis=1, inplace=True)
    fixtures_dict = fixtures.to_dict('records')
    return fixtures_dict

def edit_fixture_data(fixtures_df: pd.DataFrame) -> None:
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Man Utd', 'Manchester United')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Ipswich', 'Ipswich Town')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Man City', 'Manchester City')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace("Nott'm Forest", 'Nottingham Forest')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Newcastle', 'Newcastle United')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Spurs', 'Tottenham Hotspur')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Wolves', 'Wolverhampton Wanderers')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('West Ham', 'West Ham United')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Brighton', 'Brighton and Hove Albion')
    fixtures_df['Home Team'] = fixtures_df['Home Team'].replace('Leicester', 'Leicester City')

    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Man Utd', 'Manchester United')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Ipswich', 'Ipswich Town')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Man City', 'Manchester City')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace("Nott'm Forest", 'Nottingham Forest')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Newcastle', 'Newcastle United')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Spurs', 'Tottenham Hotspur')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Wolves', 'Wolverhampton Wanderers')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('West Ham', 'West Ham United')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Brighton', 'Brighton and Hove Albion')
    fixtures_df['Away Team'] = fixtures_df['Away Team'].replace('Leicester', 'Leicester City')