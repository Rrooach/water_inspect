from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

from water_inspect.utils.models import User

blue_auth = Blueprint('blue_auth', __name__)


@blue_auth.route('/', methods=["GET", "POST"])     # 使用多个route来绑定多个路由映射
@blue_auth.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_anonymous:
        return redirect("/index")

    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["inputEmail1"]
        password = request.form["inputPassword1"]
        user = User.query.filter_by(email=email).first()
        if user is None or not user.verify_password(password):
            return redirect(url_for("blue_auth.login"))
        login_user(user)
        flash("登录成功", "success")
        return redirect('/index')


@blue_auth.route('/logout')
@login_required
def logout():
    logout_user()

    flash("you have logout!")
    return redirect('/login')

# @blue_auth.before_request
# def auth(*args):
#     if session.get('email') is not None:
#         return redirect("/success")
#     return None
