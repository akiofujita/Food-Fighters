from flask import Flask

api = Flask(__name__)

@api.route("/")
def hello_world():
    return "<h1>Homepage</h1>"