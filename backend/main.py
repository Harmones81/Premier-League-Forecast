from config import app
from routes.general import general_routes
from routes.fixture import fixture_routes
from routes.team import team_routes
from routes.statistics import statistics_route
from routes.predictions import predictions_route

app.register_blueprint(general_routes)
app.register_blueprint(fixture_routes)
app.register_blueprint(team_routes)
app.register_blueprint(statistics_route)
app.register_blueprint(predictions_route)

if __name__ == "__main__":
    app.run(debug=True)