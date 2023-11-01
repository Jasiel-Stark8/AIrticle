"""Export Article Logic"""


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@generate.route('/export', methods=['POST'], strict_slashes=False)
def export_content():
    """Export the content to desired format"""
    content = request.form['content']
    topic = request.form['topic']
    export_format = request.form['format']

    if export_format == 'docx':
        filename = export_docx(content, topic)
    elif export_format == 'pdf':
        filename = export_pdf(content, topic)
    elif export_format == 'txt':
        filename = export_txt(content, topic)
    elif export_format == 'markdown':
        filename = export_markdown(content, topic)
    else:
        return "Unsupported Format", 400

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


def export_docx(content, topic):
    """Export content as DOCX"""
    doc = Document()
    doc.add_heading(topic, level=1)
    doc.add_paragraph(content)
    filename = secure_filename(f"{topic}.docx")
    doc.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return filename


def export_pdf(content, topic):
    """Export content as PDF"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f"{topic}.pdf"))
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.drawString(100, height - 100, content)
    c.save()
    return f"{topic}.pdf"


def export_txt(content, topic):
    """Export content as Txt"""
    filename = secure_filename(f"{topic}.txt")
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
        f.write(content)
    return filename


def export_markdown(content, topic):
    """Export content as Markdown"""
    filename = secure_filename(f"{topic}.md")
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
        f.write(f"#{topic}\n\n")
        f.write(content)
    return filename