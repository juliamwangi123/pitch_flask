from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post
 
class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def test_follow(self):
            u1 = User(username='john', email='john@example.com')
            u2 = User(username='susan', email='susan@example.com')
            db.session.add(u1)
            db.session.add(u2)
            db.session.commit()


    def test_password_hashing(self):
            u = User(username='susan')
            u.set_password('cat')
            self.assertFalse(u.check_password('dog'))
            self.assertTrue(u.check_password('cat'))
