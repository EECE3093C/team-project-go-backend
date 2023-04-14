from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    if current_user.role == 'student':
        return redirect(url_for('views.check_in'))
    else:
        return render_template("home.html", user=current_user)

@views.route('/teacher')
@login_required
def teacher_home():
    if current_user.role != 'teacher':
        return redirect(url_for('views.home'))

    attendance_records = Attendance.query.all()

    records_by_student = defaultdict(list)
    for record in attendance_records:
        records_by_student[record.student].append(record)

    students = User.query.filter_by(role='student').all()
    return render_template("teacher_home.html", students=students, records_by_student=records_by_student)

@views.route('/check-in')
@login_required
def check_in():
    return render_template("check_in.html", user=current_user)

