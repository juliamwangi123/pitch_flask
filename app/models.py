from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5

class User(UserMixin,db.Model):
    id=db.Column(db.Integer ,primary_key=True)
    username=db.Column(db.String(120),unique=True, index=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(120))
    pitch=db.relationship('Pitch' , backref='author',lazy='dynamic')


    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

            #passowrd hahing

    def set_password(self, password):
        self.password_hash =generate_password_hash(password)

        #check password
    def check_password(self , password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {} >'.format(self.username)

#userLoader

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
#generetaes user profile
def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)



class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)