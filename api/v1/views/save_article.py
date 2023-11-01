"""Save Article"""
from flask import Blueprint, abort, session, request
from models.article import Article
from database import db

save_article = Blueprint('save_article', __name__)

@save_article.route('/save_article', methods=['POST'], strict_slashes=False)
def save_article_route():
    """Save article to database"""
    user_id = session.get('user_id')
    if user_id is None:
        abort(401)

    data = request.get_json()
    topic = data.get('topic')
    content = data.get('content')

    if topic and content:
        new_article = Article(
            user_id=user_id,
            title=topic,
            content=content
        )

        db.session.add(new_article)
        db.session.commit()

        return "Article Saved", 200
    else:
        return "Problem saving article, click save again", 400
