from flask import Flask
from config import Config
from flask_cors import CORS
from app.routes.error_handlers import errors


def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    # TODO: Register every controller's blueprint
    app.register_error_handler(errors)

    return app
