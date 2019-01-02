from flask import jsonify
import water_inspect.config
from flask import Blueprint, redirect, flash, render_template, request, url_for
from flask_login import login_user, login_required
from water_inspect.app.models import User
from water_inspect.data.takeout import takeout
from water_inspect.data.cal import GM

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
        water_inspect.config.param = data['attribute']
        water_inspect.config.time = data['interval']
        # 声明一个take类
        Take = takeout(water_inspect.config.param, water_inspect.config.time)
        # 计算所需的时间
        Take.time_diff()
        TimeTable = Take.time_output()
        # 获取所需数据
        water_inspect.config.result = Take.get_data()
        # 开始生成预测序列
        m = 1
        gm = GM()
        Diff, Prb = gm.mat_cal()
        res = gm.perdict(Diff, Prb, m)
        for i in range(0, res.size):
            water_inspect.config.result.append(res[i])
        water_inspect.config.result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        info = water_inspect.config.result
        return jsonify(info)
    else:
        return render_template('index.html')

# @blue_content.before_request
# def auth(*args):
#     if session.get('email') is None:
#         return '未登录， 拦截'
#     return None

#redirect to commander page
@blue_content.route('/commander', methods=['GET', 'POST'])
def commander():
    return render_template('commander.html')

#redirect to note page
@blue_content.route('/note', methods=['GET', 'POST'])
def note():
    return render_template('note.html')
#redirect to usercommand page
@blue_content.route('/usercommand', methods=['GET', 'POST'])
def usercommand():
    return render_template('usercommand.html')