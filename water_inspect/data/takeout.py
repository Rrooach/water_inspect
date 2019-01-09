from water_inspect.app.models import Data
import water_inspect.config
from water_inspect.data.time_utils import *


# param = water_inspect.config.param
# interval = water_inspect.config.time  # type: int
# param = "wendu"
# interval = 1


class takeout():
    def __init__(self, param, interval):
        self.TimeTable = []
        self.param = param
        self.interval = interval
        # 从数据库中获取所需要的参数
        self.result = []
        self.time_dict = {}

    def data_get_hour(self):
        m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(1, 6):
            data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
            if data is None:
                m = reconvert_time(convert_time(m) - 60 * 10)
                continue
            m = reconvert_time(convert_time(m) - 60 * 10)
            if water_inspect.config.param == 'wendu':
                self.time_dict[data.time] = data.wendu
            if water_inspect.config.param == 'ph':
                self.time_dict[data.time] = data.ph
            if water_inspect.config.param == 'zhuodu':
                self.time_dict[data.time] = data.zhuodu
            if water_inspect.config.param == 'rongyang':
                self.time_dict[data.time] = data.rongyang

    def data_get_day(self):
        m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(1, 24, 2):
            data = Data.query.filter(Data.time.between(time_before_day(m), m)).first()
            if data is None:
                m = reconvert_time(convert_time(m) - 60 * 60 * 2)
                continue
            m = reconvert_time(convert_time(m) - 60 * 60 * 2)
            if water_inspect.config.param == 'wendu':
                self.time_dict[data.time] = data.wendu
            if water_inspect.config.param == 'ph':
                self.time_dict[data.time] = data.ph
            if water_inspect.config.param == 'zhuodu':
                self.time_dict[data.time] = data.zhuodu
            if water_inspect.config.param == 'rongyang':
                self.time_dict[data.time] = data.rongyang

    def data_get_week(self):
        m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(1, 7):
            data = Data.query.filter(Data.time.between(time_before_day(m), m)).first()
            if data is None:
                m = reconvert_time(convert_time(m) - 60 * 60 * 24)
                continue
            m = reconvert_time(convert_time(m) - 60 * 60 * 24)
            if water_inspect.config.param == 'wendu':
                self.time_dict[data.time] = data.wendu
            if water_inspect.config.param == 'ph':
                self.time_dict[data.time] = data.ph
            if water_inspect.config.param == 'zhuodu':
                self.time_dict[data.time] = data.zhuodu
            if water_inspect.config.param == 'rongyang':
                self.time_dict[data.time] = data.rongyang

    def data_get_month(self):
        m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(1, 30, 2):
            data = Data.query.filter(Data.time.between(time_before_month(m), m)).first()
            if data is None:
                m = reconvert_time(convert_time(m) - 60 * 60 * 24 * 2)
                continue
            m = reconvert_time(convert_time(m) - 60 * 60 * 24 * 2)
            if water_inspect.config.param == 'wendu':
                self.time_dict[data.time] = data.wendu
            if water_inspect.config.param == 'ph':
                self.time_dict[data.time] = data.ph
            if water_inspect.config.param == 'zhuodu':
                self.time_dict[data.time] = data.zhuodu
            if water_inspect.config.param == 'rongyang':
                self.time_dict[data.time] = data.rongyang

    def data_get(self):
        # 最近一个小时
        if water_inspect.config.time == '1':
            self.data_get_hour()
        # 最近一天
        if water_inspect.config.time == '2':
            self.data_get_day()
        # 最近一周
        if water_inspect.config.time == '3':
            self.data_get_week()
        # 最近一月
        if water_inspect.config.time == '4':
            self.data_get_month()

    def data_trans(self):
        TimeTable = []
        result = []
        for time, res in self.time_dict.items():
            TimeTable.append(time)
            result.append(eval(res))
        return TimeTable, result
class fake():
    def __init__(self, time, param):
        self.time = time
        self.param = param
        self.result = []
    def temp_data(self):
        if self.time == '1':
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_hour
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_hour
            if self.param == "ph":
                self.result = water_inspect.config.ph_hour
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_hour
        if self.time == '2':
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_day
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_day
            if self.param == "ph":
                self.result = water_inspect.config.ph_day
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_day
        if self.time == '3':
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_week
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_week
            if self.param == "ph":
                self.result = water_inspect.config.ph_week
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_week
        if self.time == '4':
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_month
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_month
            if self.param == "ph":
                self.result = water_inspect.config.ph_mongth
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_month
        return  self.result
# 在index.html中提供x轴数据
# 最近一小时  %H:%M
# 最近一天   %H:%M
# 最近一周   %Y-%m-%d
# 最近一个月  %m-%d


#
# #声明一个take类
# Take = takeout(param, interval)
# #计算所需的时间
# Take.time_diff()
# TimeTable = Take.time_output()
# #获取所需数据
# water_inspect.config.result = Take.get_data()


# #开始生成预测序列
# m = 1
# gm = GM()
# res = []
# Diff, Prb = gm.mat_cal()
# res = gm.perdict(Diff, Prb, m)
# length = res.size
# # for i in range(0, length):
# #     print("%lf "%res[i])
# for i in range(0, length):
#     water_inspect.config.result.append(res[i])
#
# water_inspect.config.result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
