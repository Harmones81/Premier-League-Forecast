import requests
import pandas as pd
from typing import List
from bs4 import BeautifulSoup


url = 'https://fbref.com/en/comps/9/Premier-League-Stats'


def get_team_data() -> pd.DataFrame:
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    table = soup.find('table', class_='stats_table')
    headers = table.find_all('th')
    headers = [header.text.strip() for header in headers]
    del headers[0]
    del headers[8:]
    df = pd.DataFrame(columns=headers)
    rows = table.find_all('tr')
    df = df.iloc[0:0]

    for row in rows[1:]:
        row_data = row.find_all('td')
        cell_data = [data.text.strip('+') for data in row_data]
        del cell_data[8:]
        df.loc[len(df)] = cell_data
        
    filter = ['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD']
    df[filter] = df[filter].apply(pd.to_numeric)
    return df


def teams_dict() -> List[dict]:
    df = get_team_data()
    return df.to_dict(orient='records')
