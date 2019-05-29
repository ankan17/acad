from flask_script import Manager
from werkzeug.security import generate_password_hash
from models import User
from app import db, app

manager = Manager(app)

@manager.command
def createadminuser():
  username = input("Enter username: ")
  password = input("Enter password: ")

  user = User.query.filter_by(username=username).first()

  if user:
    print("\nUser already exists!")
    exit(1)

  new_user = User(
    username=username,
    password=generate_password_hash(password, method='sha256')
  )

  db.session.add(new_user)
  db.session.commit()

  print("\nUser successfully created!")

if __name__ == "__main__":
  db.create_all()
  manager.run()
