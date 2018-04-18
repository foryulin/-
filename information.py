from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from config import Config
app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_POST)
# 对app进行保护   CSRFProtect 只做验证工作
CSRFProtect(app)
Session(app)
manger = Manager(app)
Migrate(app,db)
manger.add_command('db',MigrateCommand)
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manger.run()
