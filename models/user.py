from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config
import models

app = Flask(__name__, config)
db=SQLAlchemy(app)

class User():
    """User Signup logic"""
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(40))
    password_hash = db.Column(db.String(255))
    username = db.Column(db.String(40))

    def __init__(self, user_id, email, password_hash, username):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.username = username

    with app.app_context():
        db.create_all()
