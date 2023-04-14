from flask import Blueprint, render_template
from flask_login import current_user

# Create a blueprint for the about page
about = Blueprint('about', __name__)

# Route for the about page
@about.route('/about')
def about_page():
    description = "Welcome!"
    return render_template('about.html', user=current_user, description=description)
