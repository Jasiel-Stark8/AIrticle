""" Objects that handle all default RestFul API actions for Users:
    - Signup
    - Login
    - Logout
    - User Dashboard Session
"""
from validate_email import validate_email
from flask import flash, render_template, url_for, redirect, session, request
# from flask_login import logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from database import db

# BLUEPRINT
from flask import Blueprint
auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    """Signup logic"""
    if request.method == 'POST':
        email = request.form['email']

        # Add extra layer of abstraction | email format and domain check
        if not validate_email(email, check_mx=True):
            flash('Invalid Credentials')

        password_hash = generate_password_hash(request.form['password'])
        firstname = request.form['firstname']
        lastname = request.form['lastname']


        # Check if the user already exists
        existing_user = db.session.query(User).filter_by(email=email).first()
        try:
            if existing_user:
                flash('An account with this email already exists. Try logging in?')
            elif not email and password_hash and firstname in request.form:
                message = 'Missing credentials.'
                flash(message)
            else:
                new_user = User(email=email,
                                password_hash=password_hash,
                                firstname=firstname,
                                lastname=lastname,
                                articles=None)
                db.session.add(new_user)
                db.session.commit()
                redirect(url_for('login.html', message='Account created successfully!'))
        except Exception:
            db.session.rollback() # rollback the entire operation is anything fails


@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Login Logic"""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # No need to hash it here

        # Fetch user by email
        user = db.session.query(User).filter_by(email=email).first()

        # If user doesn't exist, or password does not match
        if not user:
            flash('Oops, Looks like you do not have an account. Kindly create one.')
        elif not check_password_hash(user.password_hash, password):
            flash('Incorrect password. Please try again!')
        else:
            session['user_id'] = user.id  # Storing user id in session
            redirect(url_for('dashboard.html', message=f'Welcome {user.firstname}'))


@auth.route('/logout', methods=['GET', 'POST'], strict_slashes=False)
def logout():
    """Logout logic"""
    session.pop('user_id', None)
    return render_template('login.html')
