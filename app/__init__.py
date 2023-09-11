from flask import Flask
from config import Config
def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    # TODO: Register every controller's blueprint

    return app
