"""Application Entry Point"""
import os
from flask import Flask, render_template, Response, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config import DevelopmentConfig, Config, OpenaiConfig, DashboardConfig
from database import db
from flask_migrate import Migrate
from io import StringIO
import csv

load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})
app.config.from_object(DevelopmentConfig)
app.config.from_object(DashboardConfig)
app.config.from_object(Config)
app.config.from_object(OpenaiConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

# Bind app to the database
db.init_app(app)

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


# Migration
migrate = Migrate(app, db)


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


# # ROOT ADMIN CONTROL BELOW
# @app.route('/admin', methods=['POST'], strict_slashes=False)
# def admin_panel():
#     """Admin Page"""
#     return render_template('admin.html')

# def download_articles():
#     # Query all articles from the database
#     articles = Article.query.all()
    
#     # Create a string buffer
#     string_buffer = StringIO()
    
#     # Create a CSV writer object using the string buffer as file
#     csv_writer = csv.writer(string_buffer)
    
#     # Write the header of the CSV file
#     csv_writer.writerow(['ID', 'User ID', 'Title', 'Content', 'Created At', 'Updated At'])

#     # Write the data rows
#     for article in articles:
#         csv_writer.writerow([
#             article.id,
#             article.user_id,
#             article.title,
#             article.content,
#             article.created_at.strftime("%Y-%m-%d %H:%M:%S"),  # Format datetime
#             article.updated_at.strftime("%Y-%m-%d %H:%M:%S")   # Format datetime
#         ])

#     # Retrieve the content of the string buffer
#     output = string_buffer.getvalue()
    
#     # Create a response object and set the appropriate headers
#     response = Response(
#         output,
#         mimetype='text/csv',
#         headers={"Content-Disposition": "attachment; filename=articles.csv"}
#     )

#     # Return the response
#     return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002)
