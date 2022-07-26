from flask import render_template, Blueprint

from datetime import datetime

from test_flask_lesson.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.context_processor
def context_processor():
    return {'now': datetime.utcnow().date()}
