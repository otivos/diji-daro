import functools

from flask import Blueprint, request, render_template, flash, redirect, url_for, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from sqlalchemy.exc import IntegrityError


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/student_registration', methods=('GET', 'POST'))
def registerStudent():
    """ Registers a new student """
    
    # grab form data.
    if request.method == 'POST':
        error = None
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username').lower()
        gender = request.form.get('gender')
        birthdate = request.form.get('birthdate')
        email = request.form.get('email')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        # ensure proper usage.
        if not firstname:
            error = "Firstname field is empty"
        if not lastname:
            error = "Lastname field is empty"
        if not username:
            error = "Username field is empty"
        if not gender:
            error = "Gender field is empty"
        if not password:
            error = "Password field is empty"
        if not password1:
            error = "Confirm password field is empty"
        if password != password1:
            error = "Passwords don't match"
        
        # persist the form data.
        if error is None:
            try:
                student = Student(firstname=firstname, lastname=lastname, username=username, gender=gender, birthdate=birthdate, email=email, password=generate_password_hash(password))
                db.session.add(student)
                db.session.commit()
            except IntegrityError as e:
                error="Request failed!. You either entered an already existing username and/or email. Please try to enter a different username and/or email."
                print(e, flush=True)
                flash(error)
                db.session.rollback()
                return render_template('auth/register.html')
            else:
                return redirect(url_for('auth.studentLogin'))

        flash(error)

    return render_template('auth/register.html')

# logs in registered students.
@bp.route('student_login', methods=('GET', 'POST'))
def studentLogin():
        
    # grab form data.
    if request.method == 'POST':
        error = None
        username = request.form.get('username').lower()
        password = request.form.get('password')
    
        # check for proper usage
        if not username:
            error = "Username field cannot be blank"
        if not password:
            error = "Password field cannot be blank"

        # retrieves student from database
        if error is None:
            student = Student.query.filter_by(username=username).all()
            if not student:
                error = "Student not found"
                print(error)

            # check if passwords match
            for row in student:
                if not check_password_hash(row.password, password):
                    error = "Incorrect password. Try again"
                else:
                    session.clear()
                    session['user_id'] = row.id
                    flash("Login successfully")
                    return redirect(url_for('index'))

        flash(error)
        
    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = Student.query.get(user_id)


# logs a user out.
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.studentLogin'))

# require authentication in other views.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.studentLogin'))
        
        return view(**kwargs)

    return wrapped_view