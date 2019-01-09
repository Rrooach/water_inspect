from flask import render_template

from .send_mail import send_mail
from .models import User


def alarm(message):
    users = User.query.all()
    for user in users:
        send_mail(user.email, "异常警告", render_template("alarm.html", message=message))
