"""Application Entry Point"""
import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config import DevelopmentConfig, Config, OpenaiConfig
from database import db

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})
app.config.from_object(DevelopmentConfig)
app.config.from_object(Config)
app.config.from_object(OpenaiConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

# Now bind the app to the database
db.init_app(app)

# Move the imports here, after the app and db are set up
from models import user
from api.v1.views.dashboard import dashboard
from api.v1.views.auth import auth

# Register the blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)

@app.route('/')
def landing_page():
    """Landing Page"""
    return render_template('landing.html')


@app.route('/sign-up')
def signup_page():
    """Sign Up Page"""
    return render_template('signup.html')


@app.route('/log-in')
def login_page():
    """Log in Page"""
    return render_template('login.html')


@app.route('/dashboard')
def home():
    """Home Page - Dashboard"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002)
