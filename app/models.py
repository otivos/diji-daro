from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class School(db.Model):
    __tablename__ = "schools"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #area = db.Column(db.String, nullable=False)

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True )
    firstname = db.Column(db.String, nullable=False )
    lastname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    gender = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)
    #school_id = db.Column(db.ForeignKey("schools.id"))
    #school = db.relationship('School', backref=db.backref('students', lazy=True))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
