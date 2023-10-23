# import uuid
# from flask import request, jsonify
# from api.v1.views import app_views
# from flask_login import login_required
# from models.autosave import Draft
# from models.save_article import Article
# from models import user
# from app import app, db
# from dotenv import load_dotenv

# load_dotenv()

# @app_views.route('/auto_save', methods=['POST'], strict_slashes=False)
# @login_required
# def auto_save():
#     """Auto save article sa draft"""
#     data = request.json()
#     content = data['article']
#     title = str(uuid.uuid4())
#     url_name = title
#     text_to_number = lambda x: None if x == '' else x
#     draft_id = text_to_number(data['draft_id'])
#     article_id = text_to_number(data['article_id'])

#     if draft_id is None:
#         """
#         Draft ID is None only when user is creating a 
#         brand new post or is editing a previous post, 
#         AND this is the very first time this API has 
#         been called for this post
#         """
#         article = Article(title=title, url_name=url_name, content=content, is_published=False)
#         db.session.add(article)
#         db.session.flush()

#         # article_id should be None is its a new article
#         draft = Draft(original_aricle_id=article_id, draft_article_id=draft_id)
#         db.session.add(draft)
#     else:
#         """
#         draft_id is not None under the following OR
#         conditions:
#         * User created new post/edit old post, and this 
#          is the 2nd through Nth time this api has 
#          been called
#         * User opens a draft. draft_id == post_id 
#           - dont make a new draft
#         """
#         article = db.session.query(Article).filter_by(id=draft_id).one()
#         db.session.add(article)

#     db.session.commit()

#     draft_id = article_id
#     return jsonify({'draft_id': draft_id}), 200
