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


if __name__ == "__main__":  
  app.run(debug=True)