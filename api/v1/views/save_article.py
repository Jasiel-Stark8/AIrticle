from flask import Blueprint, abort, session, request, jsonify
import logging
from models.article import Article
from database import db

# Changed the Blueprint name to avoid conflict
save = Blueprint('save', __name__)

@save.route('/save_article', methods=['POST'], strict_slashes=False)
def save_article_route():
    """Save article to database"""
    try:
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

            return jsonify({"message": "Article Saved"}), 200
        else:
            return jsonify({"message": "Problem saving article, please try again"}), 400

    except Exception as e:
        db.session.rollback()
        print(str(e))
        return jsonify({"message": "An error occurred while saving the article"}), 500
