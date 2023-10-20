""" Objects that handle all default RestFul API actions for Users:
    - Signup
    - Login
    - Logout
    - User Dashboard Session
"""
from validate_email import validate_email
from flask import flash, render_template, redirect, url_for, request
from flask_login import *
from werkzeug.security import generate_password_hash
from models.user import User
from app import app, db
from api.v1.views import app_views



@app.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    """Signup logic"""
    if request.method == 'POST':
        email = request.form['email']

        # Add extra layer of abstraction | email format and domain check
        if not validate_email(email, check_mx=True):
            flash('Invalid email format or domain')

        password_hash = generate_password_hash(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']


        # Check if the user already exists
        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user:
            flash('An account with this email already exists. Try logging in?')
        elif not email and not password_hash and not firstname in request.form:
            return render_template('signup_error.html',
                                   message='You have not entered some credentials.')
        else:
            new_user = User(email=email,
                            password_hash=password_hash,
                            firstname=firstname,
                            lastname=lastname)
            db.session.add(new_user)
            db.session.commit()
            return render_template('dashboard.html', message='Account created successfully!')


@app_views.route('/login', methods=['GET'], strict_slashes=False)
def login():
    """Login Logic"""
    if request.method == 'POST':
        email = request.form['email']
        password_hash = generate_password_hash(request.form['password'])

    # Double check if email and password match - paswords are hashed so how will it be verified
    user = db.session.query().filter(User(email=request.form['email']))
    if not user:
        print('Oops, Looks like you do not have an account Kindly create one')
    elif not email and not password_hash in request.form:
        return render_template('signup_error.html',
                                   message='You have not entered some credentials.')
    else:
        return render_template('dashboard.html', message=f'Welcome {user.firstname}')


@app_views.route('/logout/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def logout(id):
    """Logout logic"""
    user = db.session.query().filter(User.id == id).first()
    logout_user(user)
    return redirect('landing.html')
