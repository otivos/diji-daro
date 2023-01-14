from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Daro(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    school = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    def __repr__(self) -> str:
        return f"<Daro {self.id}, {self.firstname}, {self.lastname}, {self.username}, {self.school}, {self.password}>"





