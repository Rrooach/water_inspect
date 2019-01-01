from random import choice

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from water_inspect.app.My_token import generate_confirmation_token, confirm_token

from water_inspect.app.models import User, db
from water_inspect.app.send_mail import send_mail

blue_forget = Blueprint('blue_forget', __name__)


class Forgetform(FlaskForm):
    emial = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Submit')


@blue_forget.route("/forget", methods=["GET", "POST"])
def forget():
    form = Forgetform()
    if form.validate():
        user = User.query.filter_by(email=form.emial.data).first()
        # 判断邮箱是否存在
        if user is None:
            flash("该邮箱没有注册")
            return redirect('/forget')

        # 存在的时候生成token来进行邮箱验证
        token = generate_confirmation_token(user.email)
        confirm_url = url_for("blue_forget.confirm", token=token, _external=True)
        html = render_template("retrieve_email.html", confirm_url=confirm_url)
        subject = "Please reset your password"
        send_mail(user.email, subject, html)

        flash("An email has sent to your mailbox")
        return redirect("/login")

    return render_template('login.html', form=form)


@blue_forget.route("/forget_confirm/<token>", methods=["POST", "GET"])
def confirm(token):
    email = False
    try:
        email = confirm_token(token)
    except:
        flash("Invalid url", "danger")

    user = User.query.filter_by(email=email).first()
    new_password = "".join(
        [choice([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]) for
         i in
         range(10)])
    user.password = new_password
    db.session.add(user)
    db.session.commit()
    return "You password has reset to {}".format(new_password)
