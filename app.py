"""Application Entry point"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, Config, OpenaiConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_object(Config)
app.config.from_object(OpenaiConfig)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://airticle:220300@localhost:5432/airticle'
db = SQLAlchemy(app)

# Note: Import models and routes here AFTER creating the app and db instances.
from models import user
# Import other routes and models as needed


@app.route('/')
def home():
    return render_template('landig.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=5000)
