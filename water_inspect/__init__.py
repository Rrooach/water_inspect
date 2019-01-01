from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from water_inspect.app.models import User

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static')
bootstrap = Bootstrap(app)
loginmanager = LoginManager()

loginmanager.session_protection = "strong"
loginmanager.login_view = "blue_auth.login"
loginmanager.login_message = "你必须先登录才能访问"
loginmanager.login_message_category = "info"
app.config['SECRET_KEY'] = 'hard to guess string'
app.config["SECURITY_PASSWORD_SALT"] = "Ocean"
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['Mail_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'ocean-z@qq.com'
app.config['MAIL_PASSWORD'] = 'lubmicbncseybaij'
app.config['MAIL_DEFAULT_SENDER'] = "ocean-z@qq.com"
mail = Mail(app)

time, interval = 0, 0


# 注册蓝图
from .views.error import blue_error
app.register_blueprint(blue_error)

from .views.content import blue_content
app.register_blueprint(blue_content)

from water_inspect.views.user.auth import blue_auth
app.register_blueprint(blue_auth)

from water_inspect.views.user.account import blue_account
app.register_blueprint(blue_account)

from water_inspect.views.user.register_and_confirm import blue_register_and_confirm
app.register_blueprint(blue_register_and_confirm)

from water_inspect.views.user.forget import blue_forget
app.register_blueprint(blue_forget)

loginmanager.init_app(app)


@loginmanager.user_loader
def load_user(id):
    return User.query.filter_by(id=int(id)).first()
