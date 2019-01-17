from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

from water_inspect.utils.models import User, db
from water_inspect.utils.send_mail import send_mail
from water_inspect.utils.My_token import generate_confirmation_token, confirm_token

blue_register_and_confirm = Blueprint('blue_register_and_confirm', __name__)


class RegisterFrom(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    psw = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Submit')


@blue_register_and_confirm.route("/register", methods=["POST"])
def register():
    user = User.query.filter_by(email=request.form["inputEmail2"])
    if user is None:
        return redirect("/login")

    user = User(
        email=request.form["inputEmail2"],
        username=request.form["inputName2"],
        password=request.form["inputPassword2"],
        confirmed=False,
        is_admin=False
    )
    db.session.add(user)
    try:
        db.session.commit()
    except BaseException as e:
        print(e)
        db.session.rollback()

    token = generate_confirmation_token(user.email)
    confirm_url = url_for(
        'blue_register_and_confirm.confirm_email', token=token, _external=True)
    html = render_template('confirm_email.html', confirm_url=confirm_url)
    subject = 'Please confirm your email'
    send_mail(user.email, subject, html)

    login_user(user)

    flash("A confirmation email has been sent via email", 'success')
    return redirect("/success")


@blue_register_and_confirm.route("/confirm/<token>")
def confirm_email(token):
    email = False
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired', 'danger')

    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash("Account already confirmed. Please login", "success")
    else:
        user.confirmed = True
        db.session.add(user)
        try:
            db.session.commit()
        except BaseException as e:
            print(e)
            db.session.rollback()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect("/index")
