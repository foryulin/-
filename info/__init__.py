from flask_sqlalchemy import SQLAlchemy
import redis
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config ,config
db = SQLAlchemy()
redis_store = None

def create_app(config_name):
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
    return app

