from water_inspect.utils.models import Data
import water_inspect.config
from water_inspect.utils.time_utils import *


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
        self.TimeTable = []
    def temp_data(self):
        if self.time == '1':
            ttep = Data.query.order_by(Data.time.desc()).first()
            m = str(ttep.time)
            for i in range(1, 6):
                data = Data.query.filter(Data.time.between(time_before_hour(m), m)).first()
                if data is None:
                    m = reconvert_time(convert_time(m) - 60 * 10)
                    continue
                m = reconvert_time(convert_time(m) - 60 * 10)
                self.TimeTable.append(data.time)
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_hour
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_hour
            if self.param == "ph":
                self.result = water_inspect.config.ph_hour
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_hour
        if self.time == '2':
            ttep = Data.query.order_by(Data.time.desc()).first()
            m = str(ttep.time)
            for i in range(1, 24, 2):
                data = Data.query.filter(Data.time.between(time_before_day(m), m)).first()
                if data is None:
                    m = reconvert_time(convert_time(m) - 60 * 60 * 2)
                    continue
                m = reconvert_time(convert_time(m) - 60 * 60 * 2)
                self.TimeTable.append(data.time)
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_day
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_day
            if self.param == "ph":
                self.result = water_inspect.config.ph_day
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_day
        if self.time == '3':
            ttep = Data.query.order_by(Data.time.desc()).first()
            m = str(ttep.time)
            for i in range(1, 7):
                data = Data.query.filter(Data.time.between(time_before_day(m), m)).first()
                if data is None:
                    m = reconvert_time(convert_time(m) - 60 * 60 * 24)
                    continue
                m = reconvert_time(convert_time(m) - 60 * 60 * 24)
                self.TimeTable.append(data.time)
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_week
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_week
            if self.param == "ph":
                self.result = water_inspect.config.ph_week
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_week
        if self.time == '4':
            ttep = Data.query.order_by(Data.time.desc()).first()
            m = str(ttep.time)
            for i in range(1, 30, 2):
                data = Data.query.filter(Data.time.between(time_before_month(m), m)).first()
                if data is None:
                    m = reconvert_time(convert_time(m) - 60 * 60 * 24 * 2)
                    continue
                m = reconvert_time(convert_time(m) - 60 * 60 * 24 * 2)
                self.TimeTable.append(data.time)
            if self.param == "wendu":
                self.result = water_inspect.config.wendu_month
            if self.param == "rongyang":
                self.result = water_inspect.config.rongyang_month
            if self.param == "ph":
                self.result = water_inspect.config.ph_mongth
            if self.param == "zhuodu":
                self.result = water_inspect.config.zhuodu_month
        return self.result, self.TimeTable
