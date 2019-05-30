from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(1000), unique=True)
  password = db.Column(db.String(100))


class Contact(UserMixin , db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(1000))
	email = db.Column(db.String(1000), unique=True)
	message = db.Column(db.String(5000))
	emailto = db.Column(db.String(1000))
	copy = db.Column(db.String(1000))

	def __init__(self,name,email,message,emailto,copy):
		self.name=name
		self.email=email
		self.message=message
		self.emailto=emailto
		self.copy=copy

class Counter(db.Model):
	id=db.Column(db.Integer , primary_key=True)
	visits=db.Column(db.Integer)

	def __init__(self):
		self.visits=0

if __name__ == '__main__':
	db.create_all()
