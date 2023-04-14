from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "user.db"
DB_STUDENT_NAME = "student.db"
DB_TEACHER_NAME = "teacher.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdgjkjbmcueq'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_BINDS'] = {'student': f'sqlite:///{DB_STUDENT_NAME}', 'teacher': f'sqlite:///{DB_TEACHER_NAME}'}

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app