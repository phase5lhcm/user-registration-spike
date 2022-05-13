from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
ENV = 'dev'
app.config['SECRET_KEY'] = 'e92f34a96126929f18aff116'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if ENV == 'dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'heroku postgres db'

db = SQLAlchemy(app) # move db initialization to after config to get rid of sqlalchemy binds not being set
from signup import routes