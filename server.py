from os import environ
import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello Heruko"