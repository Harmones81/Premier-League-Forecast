from config import app
from routes.database import database_routes
from routes.fixtures import fixtures_routes
from routes.team import team_routes
from routes.statistics import statistics_route
from routes.predictions import predictions_route
from routes.status import status_routes

app.register_blueprint(database_routes)
app.register_blueprint(fixtures_routes)
app.register_blueprint(team_routes)
app.register_blueprint(statistics_route)
app.register_blueprint(predictions_route)
app.register_blueprint(status_routes)

if __name__ == "__main__":
    app.run(debug=True)