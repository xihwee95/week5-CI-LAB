import flask
import time

app = flask.Flask(name)


@app.route("/")
def index():
    return "Welcome!!! ", time.localtime