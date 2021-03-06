# encoding=utf8
from flask import Flask
import os
from flask.ext.login import LoginManager
from config import basedir
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'home'
lm.session_protection = "basic"

app.config.from_object('config')
db = SQLAlchemy(app)

from app.controller.index import *
from app.controller.articles import *
from app.controller.diffarticle import *
from app.controller.validate import *
from app.controller.weberrors import *
from app.controller.userControl import *
from app.controller.root import *
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    from logging.handlers import RotatingFileHandler

    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), MAIL_USERNAME, ADMINS, '网站崩溃了~~~', credentials,())
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

    file_handler = RotatingFileHandler('logging/mylog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.ERROR)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')


