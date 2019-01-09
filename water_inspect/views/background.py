from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user

from water_inspect.app.models import Note, User, db

blue_background = Blueprint('blue_background', __name__)


@blue_background.route('/commander', methods=['GET', 'POST'])
@login_required
def commander():
    return render_template('commander.html')


# redirect to note page
@blue_background.route('/note', methods=['GET', 'POST'])
@login_required
def note():
    noteid = request.args.get("noteid")
    if noteid is not None:
        note = Note.query.filter_by(id=noteid).first()
        db.session.delete(note)
        db.session.commit()

    notes = Note.query.all()
    return render_template('note.html', notes=notes)


# redirect to usercommand page
@blue_background.route('/usercommand', methods=['GET', 'POST'])
@login_required
def usercommand():
    if request.args.get("delete") is not None:
        user = User.query.filter_by(id=request.args["userid"]).first()
        db.session.delete(user)
        db.session.commit()
        return redirect("/usercommand")
    elif request.args.get("update") is not None:
        user = User.query.filter_by(id=request.args["userid"]).first()
        user.is_admin = True
        db.session.add(user)
        db.session.commit()
        return redirect("/usercommand")

    users = User.query.all()

    return render_template('usercommand.html', users=users)


@blue_background.before_request
def auth(*args):
    if not current_user.is_admin:
        flash("您还不是管理员")
        return redirect('/index')
    else:
        return None
