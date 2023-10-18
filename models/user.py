"""User model for PostgreSQL database"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://airticle:220300@localhost:5432/airticle'
db=SQLAlchemy(app)

class User(db.Model):
    """User Schema"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=True)

    def __init__(self, email, password_hash, firstname, lastname=None):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.firstname = firstname
        self.lastname = lastname

    with app.app_context():
        db.create_all()
