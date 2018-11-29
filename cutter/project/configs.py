"""All config options"""

import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_TEST_URL']
    