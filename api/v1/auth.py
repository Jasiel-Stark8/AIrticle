"""Authentication - Signup and Login routes"""
from models.user import User
import config
from flask import Flask, render_template, request
from sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password_hash = generate_password_hash(request.form['password'])
        username = request.form['username']

        # Check if the user already exists
        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            return render_template('signup_error.html', \
                                   message='An account with this email already exists.')
        else:
            new_user = User(email=email, password_hash=password_hash, username=username)
            db.session.add(new_user)
            db.session.commit()
            return render_template('signup_success.html', message='Account created successfully!')
