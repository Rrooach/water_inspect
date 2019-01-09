import json

from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user


import water_inspect.config
from water_inspect.app.models import Data
from water_inspect.app.time_utils import *
from water_inspect.data.cal import GM
from water_inspect.data.takeout import takeout, fake

blue_content = Blueprint('blue_content', __name__)


@blue_content.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # AJAX交互
    if request.method == "POST":
        data = json.loads(str(request.get_data(), encoding="utf-8"))
        water_inspect.config.param = data['attribute']
        water_inspect.config.time = data['interval']
        # 声明一个take类
        Take = takeout(water_inspect.config.param, water_inspect.config.time)
        # 计算所需的时间
        Take.data_get()
        # 获取所需数据
        # TimeTable ->所需要的x轴， result ->y轴
        water_inspect.config.TimeTable, water_inspect.config.result = Take.data_trans()
        m = 1
        gm = GM(water_inspect.config.result)
        try:
            Diff, Prb = gm.mat_cal()
            res = gm.perdict(Diff, Prb, m)
        except Exception:
            FAKE = fake(water_inspect.config.time, water_inspect.config.param)
            water_inspect.config.result = FAKE.temp_data()
            rres = water_inspect.config.result
            fake_water = GM(rres)
            Diff, Prb = fake_water.mat_cal()
            res = fake_water.perdict(Diff, Prb, m)
            for i in range(0, res.size):
                water_inspect.config.result.append(res[i])
            water_inspect.config.TimeTable.append("预测值")
        else:
            for i in range(0, res.size):
                water_inspect.config.result.append(res[i])
            water_inspect.config.TimeTable.append("预测值")
        x = water_inspect.config.result
        y = water_inspect.config.TimeTable

        return jsonify(x, y)

    return render_template('index.html')


@blue_content.route('/test', methods=['GET', 'POST'])
def test():
    now = '2019-01-05 16:50:00'

    data = Data.query.filter(Data.time.between(time_before_hour(now), now)).all()
    for i in data:
        print(i)
    return "Done"
