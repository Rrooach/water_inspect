from flask_mail import Message
from water_inspect import app, mail


def send_mail(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config["MAIL_DEFAULT_SENDER"]
    )
    mail.send(msg)
