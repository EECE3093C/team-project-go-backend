
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import *
from . import db
from .models import Student


# Website URLS (Routes)
views = Blueprint('views',__name__)

# Main Page
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

# Sample Database Page
@views.route('/database')
def database():
    return render_template("database.html", user=current_user)

@views.route('/students')
def show_student():
    students = db.session.query(Student).all()
    return render_template('students.html', students=students)

@views.route('/students/add', methods = ['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        student = Student(name=name, email=email)

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('show_students'))
    return render_template("students.html", user=current_user)

@views.route('/students/delete', methods=['GET','POST'])
def delete_student():
    student = request.form.get('id')
    db.session.delete(student)
    db.session.commit()

# More Information About Page
@views.route('/about')
def about():
    return render_template("about.html", user=current_user)