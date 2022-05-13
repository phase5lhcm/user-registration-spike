from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
ENV = 'prod'
app.config['SECRET_KEY'] = 'e92f34a96126929f18aff116'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('HEROKU_POSTGRESQL_URL')

db = SQLAlchemy(app) # move db initialization to after config to get rid of sqlalchemy binds not being set
from signup import routes