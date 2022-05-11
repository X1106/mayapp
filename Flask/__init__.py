import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager() 
login_manager.login_view = 'app.login'
login_manager.login_message = 'ログインしてください'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = b'TU\xa6\xfc\sfgbwrbhrwtxad\x06\x7f\xb1\xe9qP'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from Flask.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.config["MAIL_SERVER"] ='smtp.gmail.com'
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] =True
    app.config["MAIL_USERNAME"] = 'x1106ktag@gmail.com'
    app.config["MAIL_PASSWORD"] ='tpkzyweixspmmdwx'
    app.config["MAIL_DEFAULT_SENDER"] ='x1106ktag@gmail.com'
    mail = Mail(app)
    return app



