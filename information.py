from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#     redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_POST = 6379


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_POST)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
