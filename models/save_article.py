from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app import app, db

class Article(db.Model):
    """Article database schema"""
    __tablename__ = 'articles'  # Fixed the typo here
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)  # Changed to Text
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    export_format = db.Column(db.String(255))

    def __init__(self, title, content, export_format):
        self.title = title
        self.content = content
        self.export_format = export_format
