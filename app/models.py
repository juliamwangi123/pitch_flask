import email
from app import db

class User(db.Model):
    id=db.Column(db.Interger ,primary_key=True)
    username=db.Column(db.String(120),unique=True, index=True)
    email=db.column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(120))


    def __repr___(self):
        return '<User {} >'.format(self.username)

