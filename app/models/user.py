from flask_login import UserMixin
from app.extensions import db

# User (id, username, password)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'<User "{self.title}">'