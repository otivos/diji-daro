from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class School(db.Model):
    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    code = db.Column(db.String)
    area = db.Column(db.String, nullable=False)
    county = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("school_categories.id"), nullable=False)
    chartered = db.Column(db.String)


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    telephone = db.Column(db.String)
    birth_year = db.Column(db.String, nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey("schools.id"), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey("school_levels.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    created = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self) -> str:
        return f"<Daro {self.id}, {self.firstname}, {self.lastname}, {self.username}, {self.school}, {self.password}>"







