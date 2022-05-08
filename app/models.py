from datetime import datetime
from email.policy import default
from app import db

class User(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    username=db.Column(db.String(120),unique=True, index=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(120))


    def __repr__(self):
        return '<User {} >'.format(self.username)


class Pitch(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    body=db.Column(db.String(300))
    timestamp=db.Column(db.DateTime, index=True, default=datetime.now)


    def __repr__(self):
        return '<body {}'.format(self.body)