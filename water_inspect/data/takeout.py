import time
from water_inspect.app.models import Data
from flask_sqlalchemy import SQLAlchemy
from water_inspect import app
from water_inspect.views import content
import water_inspect.config
interval = water_inspect.config.interval
time = water_inspect.config.time

param = "wendu" #islong.time

def convert_time(str_time):
    # 将字符串形式的时间转换成时间戳
    return int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))

def reconvert_time(stamp):
    # 将时间戳转换成为字符串形式的时间
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))

def time_diff(interval):
    # obtain the data from last 1 hours
    print(TimeTable[0])
    if interval == 1:
        for i in range(1, 6):
            TimeTable.append(TimeTable[i - 1] - 30)
    # obtain data from last 1 days
    if interval == 2:
        for i in range(1, 24):
            TimeTable.append(TimeTable[i - 1] - 3600)
    # obtain data from last 1 weeks
    if interval == 3:
        for i in range(1, 7):
            TimeTable.append(TimeTable[i - 1] - 25200)
    # obtian data from last 1 month
    if interval == 4:
        for i in range(1, 30):
            TimeTable.append(TimeTable[i - 1] - 25200)

# time_stamp = convert_time(times)
st = Data.query.order_by(Data._time.desc()).first()
print(st._time)
TimeTable = []
TimeTable.append(st._time )
print(TimeTable[0])
time_diff(interval)
result = []
len = len(TimeTable)

# if param == 'wendu':
#     for i in range(0,len):
#         str = Data.query.filter_by(_time = TimeTable[i]).first()
#         result.append(str.wendu)
# if param == 'ph':
#     for i in range(0, len):
#         str = Data.query.filter_by(_time=TimeTable[i]).first()
#         result.append(str.ph)
# if param == 'zhuodu':
#     for i in range(0, len):
#         str = Data.query.filter_by(_time=TimeTable[i]).first()
#         result.append(str.zhoudu)
#         print(str.zhoudu)
# if param == 'rongyang':
#     for i in range(0, len):
#         str = Data.query.filter_by(_time=TimeTable[i]).first()
#         result.append(str.rongyang)
#         print(str.rongyang)
# if param == 'result':
#     len = len(TimeTable)
#     for i in len:
#         str = Data.query.filter_by(_time=TimeTable[i]).first()
#         result.append(str.result)
#         print(str.result)
res = [1,2,3,4,5,6,7,8,9]