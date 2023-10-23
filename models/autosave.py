# """Create draft model for autosave operation"""
# from flask_sqlalchemy import SQLAlchemy
# from app import app, db


# class Draft(db.Model):
#     """Draft calss in case user's browser crashes"""
#     __tablename__ = 'article_drafts'
#     id = db.Column(db.Integer, primary_key=True)
#     original_article_id = db.Column(db.Integer, db.ForeignKey('article.id', ondelete='CASCADE'), nullable=False)
#     draft_article_id = db.Column(db.Integer, db.ForeignKey('Article.id', ondelete='CASCADE'), nullable=False)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

#     __table_args__ = (
#         (db.UniqueConstraint(
#             "original_article_id",
#             "draft_article_id")
#         ),
#     )
