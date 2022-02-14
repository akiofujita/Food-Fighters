from flask_sqlalchemy import SQLAlchemy
from backend import app

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.

db = SQLAlchemy()
# login = LoginManager()
# login.login_view = "users.login"

def create_app(config_filename=None):
  """ Factory building function that creates an instance of an app """
  test = app.api
  test.config.from_pyfile(config_filename)
  return test
