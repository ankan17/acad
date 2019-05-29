from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle(
  'common.scss', 'header.scss', 'footer.scss', 'index.scss',
  filters='pyscss', output='main.css'
)
assets.register('scss_all', scss)

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

if __name__ == "__main__":  
  app.run(debug=True)