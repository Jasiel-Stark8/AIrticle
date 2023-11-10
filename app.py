"""Application Entry Point"""
import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from database import db
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Determine the configuration class based on the FLASK_ENV environment variable
config_class = DevelopmentConfig if os.getenv('FLASK_ENV') == 'development' else ProductionConfig
app.config.from_object(config_class)

# If you need to override any settings or add additional ones:
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leqmncfnxwaejk:9bcab30cd4262bcb21c09437e6d4013db6093e3be28915a7098b3f68f591bd45@ec2-3-230-24-12.compute-1.amazonaws.com:5432/d6ao2e0u8qsrmg'

# Bind app to the database
db.init_app(app)

# Migration
migrate = Migrate(app, db)

# Move the imports here, after the app and db are set up
from models import user
from models import article
from api.v1.views.auth import auth
from api.v1.views.generate import generate
from api.v1.views.save_article import save_blueprint
from api.v1.views.export_article import export

# Register the blueprints
app.register_blueprint(auth)
app.register_blueprint(generate)
app.register_blueprint(save_blueprint)
app.register_blueprint(export)

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

@app.route('/generate')
def home():
    """Home Page - generate"""
    return render_template('generate.html')

if __name__ == '__main__':
    app.run()
