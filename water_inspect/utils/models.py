import time

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, BOOLEAN, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from water_inspect import app as current_app
from water_inspect import loginmanager

db = SQLAlchemy(current_app)


@loginmanager.user_loader
def load_user(id):
    return User.query.filter_by(id=int(id)).first()


def convert_time(str_time):
    # 将字符串形式的时间转换成时间戳
    return int(time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")))


def reconvert_time(stamp):
    # 将时间戳转换成为字符串形式的时间
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp))


class Note(db.Model):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(256))
    userName = Column(String(64))
    time = Column(DateTime)

    def __init__(self, message, userName, time):
        self.message = message
        self.userName = userName
        self.time = time


class Data(db.Model):
    __tablename__ = 'data'
    time = Column(DateTime, primary_key=True)  # 时间采用时间戳的方法来存储
    wendu = Column(String(64))
    ph = Column(String(64))
    zhuodu = Column(String(64))
    rongyang = Column(String(64))
    result = Column(String(64))

    def __init__(self, time=None, wendu=None, ph=None, zhuodu=None, rongyang=None, result=None):
        self.time = time
        self.wendu = wendu
        self.ph = ph
        self.zhuodu = zhuodu
        self.rongyang = rongyang
        self.result = result


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, index=True)
    username = Column(String(64), unique=True, index=True)
    is_admin = Column(BOOLEAN)
    confirmed = Column(BOOLEAN, nullable=False)
    password_hash = Column(String(128))

    def __init__(self, email, password, username, is_admin, confirmed):
        self.email = email
        self.username = username
        self.confirmed = confirmed
        self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    def is_active(self):
        return self.confirmed

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config["SECRETE_KEY"], expiration)

        return s.dumps({'confirm': self.id})

    def __repr__(self):
        return '<User %r>' % self.username


# db.drop_all()
# db.create_all()
# u1 = User(email="982483744@qq.com", username="Ocean", password="zhangyang123", is_admin=True, confirmed=True)
# u2 = User(email="1234@qq.com", username="hsiaojz", password="zhangyang123", is_admin=False, confirmed=True)
# u3 = User(email="12345@qq.com", username="zhilishu", password="zhangyang123", is_admin=False, confirmed=False)
#
# db.session.add(u1)
# db.session.add(u2)
# db.session.add(u3)
#
# data = Data(
#     time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
#     19.3054,
#     7.6359,
#     9.9615,
#     4.6232)
# db.session.add(data)
# db.session.commit()
#
# note1 = Note(
#     "网站很好看也很实用 喜欢网站很好看也很实用 喜欢网站很好看也很实用 喜欢网站很好看也很实用 喜欢",
#     "王五",
#     time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# )
# db.session.add(note1)
#
# note2 = Note(
#     "fiusafbujiasguias",
#     "李四",
#     time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# )
# db.session.add(note2)
#
# note3 = Note(
#     "Hello World",
#     "张三",
#     time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# )
# db.session.add(note3)
# db.session.commit()
