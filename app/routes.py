from flask import render_template, request, flash, jsonify
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

def init_routes(app):

    @app.route("/") 
    def home():
        students = Student.query.all()
        for row in students:
            print(row.username)
        return render_template('index.html', students=students)
    
    # registers a new student.
    @app.route('/student_registration', methods=['GET', 'POST'])
    def registerStudent():
        
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
                    return render_template('register.html')
                else:
                    return render_template('students.html')

            flash(error)

        return render_template('register.html')

    # logs in registered students.
    @app.route('/student_login', methods=['POST', 'GET'])
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
                        flash("Login successfully")
                        return render_template('students.html')

            flash(error)
         
        return render_template('login.html')