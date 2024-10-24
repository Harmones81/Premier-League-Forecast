from config import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50), nullable=False)
    matches_played = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    loss = db.Column(db.Integer, nullable=False)
    draw = db.Column(db.Integer, nullable=False)
    goals_scored = db.Column(db.Integer, nullable=False)
    goals_conceded = db.Column(db.Integer, nullable=False)
    goal_difference = db.Column(db.Integer, nullable=False)

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'team_name': self.team_name,
            'matches_played': self.matches_played,
            'wins': self.wins,
            'loss': self.loss,
            'draw': self.draw,
            'goals_scored': self.goals_scored,
            'goals_conceded': self.goals_conceded,
            'goal_difference': self.goal_difference
        }