import redis
import logging


class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = logging.DEBUG

#     redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_POST = 6379
    # flask_session的配置信息
    SESSION_TYPE = 'redis'  # 指定session保存到redis中
    SESSION_USE_SIGNER = True  # 让cookie中的session_id被加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_POST)
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒

class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    LOG_LEVEL = logging.ERROR

class TestingConfig(Config):
    """调试模式下的配置"""
    DEBUG = True


config = {
    'development':DevelopementConfig,
    'production':ProductionConfig
}