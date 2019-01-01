from flask import jsonify
from water_inspect.data.takeout import res
import water_inspect.config
from flask import Blueprint, redirect, flash, render_template, request, url_for
from flask_login import login_user, login_required
from water_inspect.app.models import User

import json
blue_content = Blueprint('blue_content', __name__)


@blue_content.route('/', methods=['GET', 'POST'])
def index():
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


@blue_content.route('/test', methods=["GET", "POST"])
def test():
    return render_template('note.html')


@blue_content.route('/success', methods=['GET', 'POST'])
@login_required
def islog():
    if request.method == 'POST':
        data = request.get_data()
        data = str(data, encoding = "utf-8")
        data = json.loads(data)
        water_inspect.config.interval = data['id']
        water_inspect.config.time = data['time']
        info = res
        return jsonify(info)
    else:
        return render_template('index.html')

# @blue_content.before_request
# def auth(*args):
#     if session.get('email') is None:
#         return '未登录， 拦截'
#     return None
