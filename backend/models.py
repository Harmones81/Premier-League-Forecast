import requests
import pandas as pd
from bs4 import BeautifulSoup

team_page_url = 'https://fbref.com/en/comps/9/Premier-League-Stats'
player_page_url = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
season_fixtures_url = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'

def create_team_data_frame():
    team_page = requests.get(team_page_url)
    team_page_soup = BeautifulSoup(team_page.text, 'html')
    team_table = team_page_soup.find('table', class_='stats_table')
    team_table_rows = team_table.find_all('tr')
    team_data = []
    for row in team_table_rows[1:]:
        row_data = row.find_all('td')
        idv_data = [data.text.strip('+').strip() for data in row_data]
        del idv_data[8:]
        team_data.append(idv_data)
    team_dict = {'Team': [item[0] for item in team_data],
             'MP': [item[1] for item in team_data],
             'W': [item[2] for item in team_data],
             'D': [item[3] for item in team_data], 
             'L': [item[4] for item in team_data],
             'GF': [item[5] for item in team_data],
             'GA': [item[6] for item in team_data],
             'GD': [item[7] for item in team_data]}
    team_df = pd.DataFrame(team_dict)
    filter_list = ['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD']
    team_df[filter_list] = team_df[filter_list].apply(pd.to_numeric)
    team_df = team_df.set_index('Team')
    return team_df