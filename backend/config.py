from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# app configuration
app = Flask(__name__)
CORS(app)


# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///premier_league_forecast.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)