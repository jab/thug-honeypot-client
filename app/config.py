import os

class BaseConfig(object):
        DEBUG = False
        CSRF_ENABLED = True
        SECRET_KEY = os.environ['SECRET_KEY']
        MONGO_DB_URI = os.environ['MONGO_DB_URL']

class DevelopmentConfig(BaseConfig):
        DEBUG = True
        MONGO_DB_URI = os.environ['MONGO_DB_URL']

class ProductionConfig(BaseConfig):
        DEBUG = False
        MONGO_DB_URI = os.environ['MONGO_DB_URL']
