from flask_mail import Message
from water_inspect import app, mail
from flask import render_template

def send_mail(to, subject,template, message = ""):
    with app.app_context():
        msg = Message(
            subject,
            html=template,
            recipients=["731297911@qq.com"],
            body=message,
            sender=app.config["MAIL_DEFAULT_SENDER"]
        )
        mail.send(msg)