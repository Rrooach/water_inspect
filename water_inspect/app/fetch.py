import requests
import json

from flask_sqlalchemy import SQLAlchemy
from water_inspect.app.alarm import alarm
from water_inspect.app.models import *



db = SQLAlchemy(app)

CRITICAL = {
    "zhuodu_min": 100, "zhuodu_max": 500,
    "ronyang_min": 5, "rongyang_max": 10,
    "ph_min": 5, "ph_max": 8,
    "wendu_min": -1, "wendu_max": 25
}


class fetch_check():
    def __init__(self):
        self.url = "http://api.heclouds.com/devices/31026513/datastreams"
        self.API_KEY = "q2BtH6RNXehOThqL8yFBEeJWkYA="
        self.headers = {'api-key': self.API_KEY}
        self.flag = 0
        # 获得结果并打印

    # 基本设置
    def accquir(self):
        r = requests.get(self.url, headers=self.headers)
        # print(r.text + '\n')
        hjson = json.loads(r.text)

        self.time = hjson['data'][1]['update_at']
        self.wehdu = hjson['data'][1]['current_value']
        self.ph = hjson['data'][2]['current_value']
        self.zhuodu = hjson['data'][3]['current_value']
        self.rongyang = hjson['data'][4]['current_value']
        self.location = hjson['data'][5]['current_value']
        self.data = Data(time=self.time, wendu=self.wehdu, ph=self.ph, zhuodu=self.zhuodu, rongyang=self.rongyang)

        # self.__warning()

        db.session.add(self.data)
        db.session.commit()

    def __warning(self):

        message = ""

        if not 100 <= self.zhuodu <= 500:
            message += "浊度为" + str(self.zhuodu) + "\n"

        if not 5 <= self.rongyang <= 10:
            message += "溶氧量为" + str(self.rongyang) + "\n"

        if not 5 <= self.ph <= 8:
            message += "PH为" + str(self.ph) + "\n"

        if not -1 <= self.wehdu <= 25:
            message += "温度为" + str(self.wehdu) + "\n"

        if not message == "":
            return alarm(message)


f = fetch_check()
f.accquir()
