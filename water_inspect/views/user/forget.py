from random import choice
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from water_inspect.app.My_token import generate_confirmation_token, confirm_token

from water_inspect.app.models import User, db
from water_inspect.app.send_mail import send_mail

blue_forget = Blueprint('blue_forget', __name__)

executor = ThreadPoolExecutor(10)


@blue_forget.route("/forget", methods=["POST"])
def forget():
    email = request.form["forgetEmail"]
    if email is None:
        return redirect("/login")
    user = User.query.filter_by(email=email).first()
    # 判断邮箱是否存在
    if user is None:
        flash("该邮箱没有注册")
        return redirect('/login')

    # 存在的时候生成token来进行邮箱验证
    token = generate_confirmation_token(user.email)
    confirm_url = url_for("blue_forget.confirm", token=token, _external=True)
    html = render_template("retrieve_email.html", confirm_url=confirm_url)
    subject = "Please reset your password"

    executor.submit(send_mail(user.email, subject, html))

    flash("An email has sent to your mailbox")
    return redirect("/login")


@blue_forget.route("/forget_confirm/<token>", methods=["POST", "GET"])
def confirm(token):
    email = False
    try:
        email = confirm_token(token)
    except:
        flash("Invalid url", "danger")

    user = User.query.filter_by(email=email).first()

    # 生成随机密码
    new_password = "".join(
        [choice([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(0, 10)]) for
         i in range(10)])

    user.password = new_password
    db.session.add(user)
    db.session.commit()
    return "You password has reset to {}".format(new_password)
