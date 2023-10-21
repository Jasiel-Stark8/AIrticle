"""PostgreSQL Airticle Database"""

class Article(db.Model):
    """Article database schema"""
    __tablename__ = 'airticles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, db.ForeignKey(User))
    title = db.Column(db.String(255))
    content = db.Column(db.Text(5000))
    last_saved = db.Column(db.TimeField((""), auto_now=True, auto_now_add=True))
    export_format = db.Column(db.String(255))
