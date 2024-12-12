import os
import requests
import pandas as pd

teams_url = 'https://www.skysports.com/premier-league-table'

img_urls = [
    'https://loodibee.com/wp-content/uploads/Liverpool-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Arsenal-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Chelsea-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Brighton-Hove-Albion-logo.png',
    'https://loodibee.com/wp-content/uploads/Manchester-City-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Nottingham-Forest-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Tottenham-Hotspur-logo.png',
    'https://loodibee.com/wp-content/uploads/Brentford-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Manchester-United-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Fulham-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Newcastle-United-logo.png',
    'https://loodibee.com/wp-content/uploads/Aston-Villa-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/AFC-Bournemouth-logo.png',
    'https://loodibee.com/wp-content/uploads/West-Ham-United-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Leicester-City-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Crystal-Palace-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Everton-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Wolverhampton-Wanderers-logo.png',
    'https://loodibee.com/wp-content/uploads/Ipswich-Town-FC-logo.png',
    'https://loodibee.com/wp-content/uploads/Southampton-FC-logo.png',
]

fixtures_url = 'https://fixturedownload.com/results/epl-2024'

def scrape_team_data() -> list[dict]:
    teams = pd.read_html(teams_url)[0]
    teams.drop('Position', axis=1, inplace=True)
    teams.columns = ['Team', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
    filenames = save_img(img_urls)
    teams['Logo'] = filenames
    teams_dict = teams.to_dict(orient='records')
    return teams_dict

def scrape_fixture_data() -> list[dict]:
    fixtures = pd.read_html(fixtures_url)[0]
    edit_fixture_data(fixtures)
    fixtures.columns = ['Gameweek', 'Date', 'Location', 'Home', 'Away', 'Result']
    fixtures['Date'] = pd.to_datetime(fixtures['Date'])
    fixtures_dict = fixtures.to_dict('records')
    return fixtures_dict

def save_img(img_urls: list[str]) -> list[str]:
    filenames = []
    # Create the folder if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    for i, url in enumerate(img_urls):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Check if the request was successful
            # Create a unique filename for each image
            file_extension = url.split('.')[-1].split('?')[0]  # Handle query params in URLs
            filename = os.path.join('images', f"logo_{i + 1}.{file_extension}")
            filenames.append(filename)
            # Write the content to a file
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Image {i + 1} saved as {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image {i + 1} from {url}. Error: {e}")
    return filenames

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