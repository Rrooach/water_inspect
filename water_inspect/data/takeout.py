import time
from water_inspect.app.models import Data
import water_inspect.config
from  water_inspect.data.time_utils import *
from sqlalchemy import extract, and_

# param = water_inspect.config.param
# interval = water_inspect.config.time  # type: int
# param = "wendu"
# interval = 1





class takeout():
    def __init__(self, param, interval):
        self.TimeTable = []
        self.param = param
        self.interval = interval
        # 获取数据库最近一条数据的时间
        st = Data.query.order_by(Data.time.desc()).first()
        self.TimeTable.append(st.time)
        #从数据库中获取所需要的参数
        self.result = []
        self.time_dict = {}

    def convert_time(str_time):
        # 将字符串形式的时间转换成时间戳
        return int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))

    def reconvert_time(stamp):
        # 将时间戳转换成为字符串形式的时间
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))
    def data_get(self):
        #最近一个小时
        if water_inspect.config.result == 1:
            st = Data.query.order_by(Data.time.desc()).first()
            if water_inspect.config.param == 'wendu':
                m = st.time
                self.time_dict[m] = st.wendu
                for i in range(1, 6):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.wendu
                    m -= 60*10
            if water_inspect.config.param == 'ph':
                m = st.time
                self.time_dict[m] = st.ph
                for i in range(1, 6):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.ph
                    m -= 60 * 10
            if water_inspect.config.param == 'zhuodu':
                m = st.time
                self.time_dict[m] = st.zhuodu
                for i in range(1, 6):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.zhuodu
                    m -= 60*10
            if water_inspect.config.param == 'rongyang':
                m = st.time
                self.time_dict[m] = st.rongyang
                for i in range(1, 6):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.rongyang
                    m -= 60*10
        #最近一天
        if water_inspect.config.result == 2:
            st = Data.query.order_by(Data.time.desc()).first()
            if water_inspect.config.param == 'wendu':
                m = st.time
                self.time_dict[m] = st.wendu
                for i in range(1, 24, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.wendu
                    m -= 60*60*2
            if water_inspect.config.param == 'ph':
                m = st.time
                self.time_dict[m] = st.ph
                for i in range(1, 24, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.ph
                    m -= 60 * 60 * 2
            if water_inspect.config.param == 'zhuodu':
                m = st.time
                self.time_dict[m] = st.zhuodu
                for i in range(1, 24, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.zhuodu
                    m -= 60 * 60 * 2
            if water_inspect.config.param == 'rongyang':
                m = st.time
                self.time_dict[m] = st.rongyang
                for i in range(1, 24, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.rongyang
                    m -= 60 * 60 * 2
        #最近一月
        if water_inspect.config.result == 3:
            st = Data.query.order_by(Data.time.desc()).first()
            if water_inspect.config.param == 'wendu':
                m = st.time
                self.time_dict[m] = st.wendu
                for i in range(1, 7):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.wendu
                    m -= 60*60*24
            if water_inspect.config.param == 'ph':
                m = st.time
                self.time_dict[m] = st.ph
                for i in range(1, 7):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.ph
                    m -= 60 * 60 * 24
            if water_inspect.config.param == 'zhuodu':
                m = st.time
                self.time_dict[m] = st.zhuodu
                for i in range(1, 7):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.zhuodu
                    m -= 60 * 60 * 24
            if water_inspect.config.param == 'rongyang':
                m = st.time
                self.time_dict[m] = st.rongyang
                for i in range(1, 7):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.rongyang
                    m -= 60 * 60 * 24
        #最近一周
        if water_inspect.config.result == 4:
            st = Data.query.order_by(Data.time.desc()).first()
            if water_inspect.config.param == 'wendu':
                m = st.time
                self.time_dict[m] = st.wendu
                for i in range(1, 30, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.wendu
                    m -= 60*60*24*2
            if water_inspect.config.param == 'ph':
                m = st.time
                self.time_dict[m] = st.ph
                for i in range(1, 30, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.ph
                    m -= 60 * 60 * 24 * 2
            if water_inspect.config.param == 'zhuodu':
                m = st.time
                self.time_dict[m] = st.zhuodu
                for i in range(1, 30, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.zhuodu
                    m -= 60 * 60 * 24 * 2
            if water_inspect.config.param == 'rongyang':
                m = st.time
                self.time_dict[m] = st.rongyang
                for i in range(1, 30, 2):
                    data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                    time[data.time] = data.rongyang
                    m -= 60 * 60 * 24 * 2
    def data_trans(self):
        TimeTable = []
        result = []
        for time, res in self.time_dict.items():
            TimeTable.append(time)
            result.append(res)
        return TimeTable, result
    #在index.html中提供x轴数据
    # 最近一小时  %H:%M
    # 最近一天   %H:%M
    # 最近一周   %Y-%m-%d
    # 最近一个月  %m-%d
    # def time_output(self):
    #     time_x = []
    #     # obtain the data from last 1 hours
    #     if self.interval == 1:
    #         for i in range(0, 6):
    #             time_x.append(time.strftime('%M:%S', time.localtime(self.TimeTable[i])))
    #     # obtain data from last 1 days
    #     if self.interval == 2:
    #         for i in range(0, 24):
    #             time_x.append(time.strftime('%M:%S', time.localtime(self.TimeTable[i])))
    #     # obtain data from last 1 weeks
    #     if self.interval == 3:
    #         for i in range(0, 7):
    #             time_x.append(time.strftime('%Y-%m-%d', time.localtime(self.TimeTable[i])))
    #     # obtian data from last 1 month
    #     if self.interval == 4:
    #         for i in range(0, 30):
    #             time_x.append(time.strftime('%Y-%m-%d', time.localtime(self.TimeTable[i])))
    #     return time_x
    #
    # def get_data(self):
    #     length = len(self.TimeTable)
    #     if self.param == 'wendu':
    #         for i in range(0,length):
    #             str = Data.query.filter_by(_time = self.TimeTable[i]).first()
    #             self.result.append(str.wendu)
    #     if self.param == 'ph':
    #         for i in range(0, length):
    #             str = Data.query.filter_by(_time = self.TimeTable[i]).first()
    #             self.result.append(str.ph)
    #     if self.param == 'zhuodu':
    #         for i in range(0, length):
    #             str = Data.query.filter_by(_time = self.TimeTable[i]).first()
    #             self.result.append(str.zhuodu)
    #             print(str.zhuodu)
    #     if self.param == 'rongyang':
    #         for i in range(0, length):
    #             str = Data.query.filter_by(_time = self.TimeTable[i]).first()
    #             self.result.append(str.rongyang)
    #             print(str.rongyang)
    #     # if param == 'result':
    #     #     for i in range(0, length):
    #     #         str = Data.query.filter_by(_time = self.TimeTable[i]).first()
    #     #         self.result.append(str.result)
    #     #         print(str.result)
    #     return  self.result

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