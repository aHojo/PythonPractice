# Templates are in jinja
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "Nina"
    # return "Hello World"
    return render_template("index.html", name=name)


@app.route("/france")
def bonjour_world():
    return "Bonjour World"


@app.route("/name/<name>")
def hello_name(name):
    return f"Hello {name}"


# FLASK_APP=helloW.py flask run
# FLASK_APP=helloW.py FLASK_ENV=developmentflask run

# Windows
# $env:FLASK_APP = helloW.py; flask run
# $env:FLASK_APP = helloW.py;$env:FLASK_ENV = 'development'; flask run
