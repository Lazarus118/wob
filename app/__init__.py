from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.login import LoginManager
from flask.ext.mail import Mail


app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)

# Setup SQLAlchemy for the project
db = SQLAlchemy(app)

# LoginManager is needed for the login process
lm = LoginManager()
lm.session_protection = "strong"
lm.setup_app(app)

from app import views, models
