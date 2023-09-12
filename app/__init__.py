from flask import Flask
from config import Config
from flask_cors import CORS
def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    # TODO: Register every controller's blueprint

    return app
