"""Authentication - Signup and Login routes"""
from flask import render_template, request
from werkzeug.security import generate_password_hash
from models.user import User
from app import db


@app.route('/signup', methods=['POST'])
def signup():
    """Signup logic"""
    if request.method == 'POST':
        email = request.form['email']
        password_hash = generate_password_hash(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        # Check if the user already exists
        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            return render_template('signup_error.html', \
                                   message='An account with this email already exists.')
        else:
            new_user = User(email=email,
                            password_hash=password_hash,
                            firstname=firstname,
                            lastname=lastname)
            db.session.add(new_user)
            db.session.commit()
            return render_template('signup_success.html', message='Account created successfully!')
