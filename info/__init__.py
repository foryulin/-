from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
import redis
import logging
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config ,config
db = SQLAlchemy()
redis_store = None

def stup_log(config_name):
    """配置日志"""
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("/home/python/Desktop/Flask02项目/logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    stup_log(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_POST)
    # 对app进行保护   CSRFProtect 只做验证工作
    CSRFProtect(app)
    # 设置app的保存位置
    Session(app)
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    return app

