#!venv/bin/python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration for SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Configuration MongoAlchemy
#MONGOALCHEMY_DATABASE = "flasktest"

# Used for WTForms
CSRF_ENABLED = True
SECRET_KEY = "justAs1mPl3K3yzT0t357"

# Configuration for Email 
DEBUG = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'austin.lazarus@gmail.com'
MAIL_PASSWORD = 'GetFitAustin'

# administrator list
ADMINS = ['austin.lazarus@gmail.com']