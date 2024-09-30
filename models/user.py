from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(220), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'
