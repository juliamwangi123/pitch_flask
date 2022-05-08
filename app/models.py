from datetime import datetime
from email.policy import default
from app import db

class User(db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    username=db.Column(db.String(120),unique=True, index=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(120))
    pitch=db.relationship('Pitch' , backref='author',lazy='dynamic')

    def __repr__(self):
        return '<User {} >'.format(self.username)


class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)