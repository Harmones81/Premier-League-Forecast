from flask import Flask
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

app.config.from_prefixed_env('APP')
MONGO_URI = app.config['MONGO_URI']
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

main_db = client['premier_league_forecast']
team_db = main_db['teams']
fixture_db = main_db['fixtures']