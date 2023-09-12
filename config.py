from dotenv import dotenv_values

class Config:
    config = dotenv_values('.env')
    SECRET_KEY = config["SECRET_KEY"]

    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    DATABASE_NAME = 'chatify'
    DATABASE_USERNAME = 'admin'
    DATABASE_PASSWORD = 'admin'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '3306'
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
