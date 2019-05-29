from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(1000), unique=True)
  password = db.Column(db.String(100))