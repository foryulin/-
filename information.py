from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
