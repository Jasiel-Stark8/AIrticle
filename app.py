"""Application Entry Point"""
import os
from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, Config, OpenaiConfig
from dotenv import load_dotenv
from api.v1.views import app_views

load_dotenv()
app = Flask(__name__)
cors = CORS(app, resources={r"/api/v1/*": {"app": "0.0.0.0"}})
app.config.from_object(DevelopmentConfig)
app.config.from_object(Config)
app.config.from_object(OpenaiConfig)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://airticle:220300@localhost:5432/airticle'
app.register_blueprint(app_views)
db = SQLAlchemy(app)


# Import models and routes here AFTER creating the app and db instances.
from models import user
# from models import save_article
# from models import autosave
# from api.v1.views import gpt
# from api.v1.views import auth
# from api.v1.views import autosave


@app.route('/')
def home():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
