import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True if os.getenv('FLASK_ENV') == 'development' else False    

class DatabaseConfig(Config):
    POSTGRESQL_DATABSAE_URI = os.getenv('POSTGRESQL_DATABSAE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class OpenaiConfig(Config):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    