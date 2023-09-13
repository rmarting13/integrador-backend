from flask import Flask

from app.routes.user_bp import user_bp
from config import Config
from flask_cors import CORS
from app.routes.error_handlers import errors


def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    # TODO: Register every controller's blueprint
    app.register_blueprint(errors)
    app.register_blueprint(user_bp)

    return app
