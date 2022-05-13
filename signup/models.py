from flask_sqlalchemy import SQLAlchemy
from signup import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False,unique=True)
    
    def __init__(self, username):
        self.username = username
        
   

    
    