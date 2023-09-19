from dotenv import dotenv_values


class Config:
    config = dotenv_values('.env')

    SECRET_KEY = config.get('SECRET_KEY')
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True

    DATABASE_USERNAME = config.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = config.get('DATABASE_PASSWORD')
    DATABASE_HOST = config.get('DATABASE_HOST')
    DATABASE_PORT = config.get('DATABASE_PORT')

    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
