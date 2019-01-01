from flask import Blueprint, session, redirect, flash, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_login import login_user, logout_user, login_required
from water_inspect.app.models import User

blue_auth = Blueprint('blue_auth', __name__)


class NameForm(FlaskForm):
    name = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    psw = PasswordField('Password', validators=[DataRequired()])
    remeber_me = BooleanField('keep me login')
    submit = SubmitField('Submit')


@blue_auth.route('/login', methods=['GET', 'POST'])
def login():
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
        return redirect('/success')


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
