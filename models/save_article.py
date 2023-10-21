"""PostgreSQL Airticle Database"""
from datetime import datetime
from flask_sqlalchemy import sqlalchemy
from app import app, db

class Article(db.Model):
    """Article database schema"""
    __tablename__ = 'airticles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, db.ForeignKey(User))
    title = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    export_format = db.Column(db.String(255))


    def __init__(self, title, created_on, updated_on, export_format):
        self.title = title
        self.created_on = created_on
        self.updated_on = updated_on
        self.export_format = export_format
