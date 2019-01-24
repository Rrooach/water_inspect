from flask import render_template, Blueprint
from water_inspect import app
from .send_mail import send_mail
from .models import User
blue_alarm = Blueprint('alarm', __name__)
def alarm(message):
    with app.app_context():
        users = User.query.all()
        html = render_template('alarm.html', msg = message)  # type: object
        for user in users:
            send_mail(user.email, "异常警告", render_template('alarm.html', msg = message), message)
