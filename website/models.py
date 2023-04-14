from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    role = db.Column(db.String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

# # Inherits from Person: student_id, major, check_in (Attendence)
class Student(db.Model):
    __bind_key__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

class Teacher(db.Model):
    __bind_key__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

# # Inherits from Person: teacher_id
# class Teacher(Person):
#     pass

