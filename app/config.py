import os

class BaseConfig(object):
        CSRF_ENABLED = True
        SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
        MONGO_DB_URI = os.environ.get('MONGO_DB_URL', 'mongodb://localhost:27017/thug')

class DevelopmentConfig(BaseConfig):
        DEBUG = True

class ProductionConfig(BaseConfig):
        DEBUG = False

DefaultConfig = DevelopmentConfig
