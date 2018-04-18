from flask_sqlalchemy import SQLAlchemy
import redis
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)
# 配置redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_POST)
# 对app进行保护   CSRFProtect 只做验证工作
CSRFProtect(app)
# 设置app的保存位置
Session(app)
