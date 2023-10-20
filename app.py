"""Application Entry Point"""
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, Config, OpenaiConfig
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_object(Config)
app.config.from_object(OpenaiConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://airticle:220300@localhost:5432/airticle'
db = SQLAlchemy(app)


# JASON: Import models and routes here AFTER creating the app and db instances.
from models import user
# from models import article
# from models import autosave
# from api.v1.views import articles
# from api.v1.views import auth
# from api.v1.views import autosave
# Import other routes and models as needed

@app.route('/')
def home():
    return render_template('landig.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
