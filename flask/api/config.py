import os
from typing import Optional

from dotenv import load_dotenv
from flask import Flask


load_dotenv()


class Config(object):

    def __init__(self) -> None:
        self.BASEDIR = os.path.dirname(__file__)
        self.ENV = os.environ.get('FLASK_ENV')
        self.SECRET_KEY: str = os.environ.get('SECRET_KEY')


class ProductionConfig(Config):

    def __init__(self) -> None:
        super().__init__()

        self.DEBUG = False

        # Flask-SQLAlchemy
        self.DB_SCHEMA: str = os.environ.get('DB_SCHEMA')
        self.DB_NAME: str = os.environ.get('DB_NAME')
        self.DB_USER: str = os.environ.get('DB_USER')
        self.DB_PASS: str = os.environ.get('DB_PASS')
        self.DB_HOST: str = os.environ.get('DB_HOST')
        self.DB_PORT: str = os.environ.get('DB_PORT')
        self.SQLALCHEMY_DATABASE_URI: str = f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        self.SQLALCHEMY_TRACK_MODIFICATIONS: bool = True if os.environ.get(
            'SQLALCHEMY_TRACK_MODIFICATIONS').lower() == 'true' else False

        # Redis
        # self.REDIS_HOST: str = os.environ.get('REDIS_HOST')
        # self.REDIS_PORT: int = int(os.environ.get('REDIS_PORT'))
        # self.REDIS_DB: int = int(os.environ.get('REDIS_DB'))
        # self.REDIS_EXPIRE: int = int(os.environ.get('REDIS_EXPIRE'))


class DevelopmentConfig(Config):

    def __init__(self) -> None:
        super().__init__()

        self.DEBUG = True

        # Flask-SQLAlchemy
        self.DB_SCHEMA: str = os.environ.get('DB_SCHEMA')
        self.DB_NAME: str = os.environ.get('DB_NAME')
        self.DB_USER: str = os.environ.get('DB_USER')
        self.DB_PASS: str = os.environ.get('DB_PASS')
        self.DB_HOST: str = os.environ.get('DB_HOST')
        self.DB_PORT: str = os.environ.get('DB_PORT')
        self.SQLALCHEMY_DATABASE_URI: str = f'postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        self.SQLALCHEMY_TRACK_MODIFICATIONS: bool = True if os.environ.get(
            'SQLALCHEMY_TRACK_MODIFICATIONS').lower() == 'true' else False

        # Redis
        # self.REDIS_HOST: str = os.environ.get('REDIS_HOST')
        # self.REDIS_PORT: int = int(os.environ.get('REDIS_PORT'))
        # self.REDIS_DB: int = int(os.environ.get('REDIS_DB'))
        # self.REDIS_EXPIRE: int = int(os.environ.get('REDIS_EXPIRE'))


def _env_choose() -> Optional[DevelopmentConfig | ProductionConfig]:
    _config = Config()
    if _config.ENV == 'development':
        APP_CONFIG = DevelopmentConfig()
    elif _config.ENV == 'production':
        APP_CONFIG = ProductionConfig()
    else:
        APP_CONFIG = DevelopmentConfig()
    return APP_CONFIG


APP_CONFIG = _env_choose()


def load_app_config(app: Flask) -> None:
    app.config.from_object(APP_CONFIG)
