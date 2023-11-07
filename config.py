"""Application Configuration"""
import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True if os.getenv('FLASK_ENV') == 'development' else False
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRESQL_DATABASE_URI')

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('POSTGRESQL_DATABASE_URI')

class OpenaiConfig():
    """OpenAI configuration"""
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class DashboardConfig():
    """Configuration for dashboard"""
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
