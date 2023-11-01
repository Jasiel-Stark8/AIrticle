"""
    - Save articles
    - Query and display articles by user id
"""
from flask import Flask, redirect, render_template, request, Blueprint, abort, send_from_directory, jsonify, session
import markdown
import os
from flask_sqlalchemy import SQLAlchemy
from models.article import Article
from app import app
from database import db
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

export = Blueprint('export', __name__)

UPLOAD_FOLDER = 'exports/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'md'}

@export.route('/save_article', methods=['POST'], strict_slashes=False)
def save_article():
    """Save article to database"""
    user_id = session.get('user_id')
    if user_id is None:
        abort(401)
    else:
        topic = request.form['topic']
        content = request.form['content']

        new_article = Article(
            user_id=user_id,
            title=topic,
            content=content
        )
        new_article.user_id = session.id

        db.session.add(new_article)
        db.session.commit()

        return "Article Saved", 200
    # else:
    #     return "Problem saving article, click save again", 400
