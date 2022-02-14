from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
# login = LoginManager()
# login.login_view = "users.login"


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    db.init_app(app)
    return app
