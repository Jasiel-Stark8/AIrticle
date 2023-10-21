from flask import Flask, render_template, request
from api.v1.views import auth
from api.v1.views import autosave
from api.v1.views import gpt
from api.v1.views.gpt import generate_article
from api.v1.views import app_views
from models import save_article
from app import app, db
from flask_login import login_required

# Generate Button Logic
@app_views.route('/generate', methods=['POST'], strict_slashes=False)
@login_required
def generate_content():
    """Get article parameters from client to feed to GPT"""
    topic = request.form['topic']
    keywords = request.form['keywords'].split(',')
    article_length = request.form['article_length']

    article = generate_article(topic, keywords, article_length)    

    return render_template('dashboard.html', article=article)
