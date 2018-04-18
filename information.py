from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#     redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_POST = 6379
    # flask_session的配置信息
    SESSION_TYPE = 'redis'  # 指定session保存到redis中
    SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_POST)
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_POST)
# 对app进行保护   CSRFProtect 只做验证工作
CSRFProtect(app)
Session(app)
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
