import requests
import json
from water_inspect.app.models import *

db = SQLAlchemy(app)

# 基本设置
class FETCH:
    def __init__(self):
        self.url = "http://api.heclouds.com/devices/31026513/datastreams"
        API_KEY = "q2BtH6RNXehOThqL8yFBEeJWkYA="
        self.headers = {'api-key': API_KEY}

    def acquire(self):
        # 获得结果并打印
        r = requests.get(self.url, headers=self.headers)
        # print(r.text + '\n')
        hjson = json.loads(r.text)
        self.time = hjson['data'][1]['update_at']
        self.wehdu = hjson['data'][1]['current_value']
        self.ph = hjson['data'][2]['current_value']
        self.zhuodu = hjson['data'][3]['current_value']
        self.rongyang = hjson['data'][4]['current_value']
        self.location = hjson['data'][5]['current_value']
        self.accumulate = hjson['data'][6]['current_value']

    def upload(self):
        data = Data(time = self.time, wendu = self.wehdu, ph = self.ph, zhuodu = self.zhuodu, rongyang = self.rongyang)
        db.session.add(data)
        db.session.commit()

fetch = FETCH()
fetch.acquire()
fetch.upload()
