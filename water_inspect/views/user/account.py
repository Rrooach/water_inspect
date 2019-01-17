from flask import Blueprint, render_template, session
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from water_inspect.utils.models import User, db

blue_account = Blueprint('blue_account', __name__, url_prefix='/account')


class NameForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    psw = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Submit')


class delForm(FlaskForm):
    email = StringField('Email', validators=[
                        DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Submit')


@blue_account.route('/modify', methods=['GET', 'POST'])
@login_required
def modify():
    form = NameForm()
    form.email.data = session.get('email')
    form.name.data = session.get('name')
    if form.validate_on_submit():
        email = form.email.data
        psw = form.psw.data
        db.session.query(User).filter(
            User.email == email).update({"password_hash": psw})
        try:
            db.session.commit()
        except BaseException as e:
            print(e)
            db.session.rollback()
    return render_template('login.html', form=form, flag='Modify')


@blue_account.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = delForm()
    if form.validate_on_submit():
        email = form.email.data
        # 通过session查询User类，然后过滤出id>5的进行删除
        db.session.query(User).filter(User.email == email).delete()
        try:
            db.session.commit()
        except BaseException as e:
            print(e)
            db.session.rollback()
    return render_template('login.html', form=form, flag='Delete')
