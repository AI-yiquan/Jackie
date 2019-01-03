# --*-- coding:utf-8 --*--
import logging
from redis import StrictRedis

class Config(object):
    """应用程序配置类"""
    # 开启调试模式
    DEBUG = None

    # logging等级
    LOGGIONG_LEVEL = logging.DEBUG

    # 配置secret key,简单生成方法，ipthon 中 base64.b64encode(os.urandom(48))
    SECRET_KEY='ix4En7l1Hau10aPq8kv8tuzcVl1s2Zo6eA+5+R+CXor8G3Jo0IJvcj001jz3XuXl'

    # 连接数据库
    SQLALCHEMY_DATABASE_URI='mysql://root:mysql@127.0.0.1:3306/ihome'
    # 是否开启追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置Redis数据库
    REDIS_HOST='127.0.0.1'
    REDIS_PORT = 6379

    # 配置session数据存储到redis数据库
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 3600 * 24


class DevelopConfig(Config):
    """开发阶段下的配置子类"""
    DEBUG = True
    LOGGIONG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产环境下配置子类"""
    DEBUG = False
    LOGGIONG_LEVEL = logging.WARNING


# 工厂函数原材料
configs={
    'default': Config,
    'develop': DevelopConfig,
    'production': ProductionConfig
}