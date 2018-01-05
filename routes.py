from flask import Flask, render_template
from models import db
from form import SignupForm

app = Flask(__name__)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)


app.secret_key = "develompent-key"


# render the homepage
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/signup")
def signup():
	form = SignupForm()
	return render_template("signup.html", form=form)



if __name__ == "__main__":
  app.run(debug=True)