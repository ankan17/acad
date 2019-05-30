from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.security import check_password_hash
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy(app)
migrate=Migrate(app,db)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle(
  'common.scss', 'header.scss', 'footer.scss', 'index.scss',
  'contact.scss', 'login.scss',
  filters='pyscss', output='main.css'
)
assets.register('scss_all', scss)

@login_manager.user_loader
def load_user(user_id):
  from models import User
  return User.query.get(int(user_id))

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/letter_president")
def letter_president():
	return render_template('letter_president.html')

@app.route("/basic_membership")
def basic_membership():
	return render_template('basic_membership.html')

@app.route("/senior_membership")
def senior_membership():
	return render_template('senior_membership.html')

@app.route("/board_of_directors")
def board_of_directors():
	return render_template('board_of_directors.html')

@app.route("/conferences")
def conferences():
	return render_template('conferences.html')

@app.route("/journals")
def journals():
	return render_template('journal.html')

@app.route("/proceedings")
def proceedings():
	return render_template('proceedings.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')

@app.route("/contact",methods=['POST'])
def contact_form():
	name = request.form['name']
	email = request.form['email']
	message = request.form['message']
	emailTo = request.form['emailTo']
	copyOfEmail = request.form['copy']

	from models import Contact
	contact = Contact(name=name,email=email,message=message,emailto=emailTo,copy=copyOfEmail)
	db.session.add( contact )
	db.session.commit()

	print(name,email,message,emailTo,copyOfEmail)
	return render_template('contact.html')

@app.route("/admin")
def admin():
	if not current_user.is_authenticated:
		return render_template('login.html')
	else:
		from models import Contact
		response = Contact.query.all()
		content ={'contact':response,'name':current_user.username}
		return render_template('messages.html',content=content)

@app.route('/login', methods=['POST'])
def login():
  username = request.form.get('username')
  password = request.form.get('password')

  from models import User
  user = User.query.filter_by(username=username).first()

  if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')

  login_user(user)
  return redirect(url_for('admin'))

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('admin'))


if __name__ == "__main__":
  	db.create_all()
  	app.run(debug=True)
