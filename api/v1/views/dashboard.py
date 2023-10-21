from flask import Flask, render_template, request
from api.v1.views import auth
from api.v1.views import autosave
from api.v1.views import gpt
from api.v1.views.gpt import generate_article
from api.v1.views import app_views
from models import save_article
from app import app, db
from flask_login import login_required
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Generate Button Logic
@app_views.route('/generate', methods=['POST'], strict_slashes=False)
@login_required
def generate_content():
    """Get article parameters from client to feed to GPT"""
    topic = request.form['topic']
    keywords = [k.strip() for k in request.form['keywords'].split(',')]
    article_length = request.form['article_length']

    article = generate_article(topic, keywords, article_length)

    return render_template('dashboard.html', article=article)


@app_views.route('export')
@login_required
def export_docx():
    """Export article as DOCX"""
    doc = Document()
    doc.add_heading('{topic}')
    doc.add_paragraph('{article}')
    doc.save('{topic}.docx')


def export_pdf():
    """Export article as PDF"""
    file = canvas.Canvas('{topic}.pdf', pagesize=letter)
    width, height = letter
    file.drawString(100, height - 100, '{article}')
    file.save()


def export_txt():
    """Export article as Txt"""
    pass


def export_markdown():
    """Export article as Markdown"""
    pass
