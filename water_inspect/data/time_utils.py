import time


def convert_time(str_time):
    # 将字符串形式的时间转换成时间戳
    return int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))


def reconvert_time(stamp):
    # 将时间戳转换成为字符串形式的时间
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))


def time_before_hour(now=None):
    if now is None:
        now = int(time.time())
    else:
        now = convert_time(now)

    return reconvert_time(now - 600)


def time_before_day(now=None):
    if now is None:
        now = int(time.time())
    else:
        now = convert_time(now)

    return reconvert_time(now - 3600 * 24)


def time_before_month(now=None):
    if now is None:
        now = int(time.time())
    else:
        now = convert_time(now)

    return reconvert_time(now - 3600 * 24 * 30)
